import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from datetime import datetime
from river3_vactor import River
class BatchInflow:
    """
    支持手动指定起始时间戳，并只对该时间之后的数据计算秒差并插值。
    """
    def __init__(self, path: str, start_time: str | datetime):
        # 1. 读取并清理
        df = (pd.read_csv(path, sep='\t', encoding='gbk',
                          engine='python', on_bad_lines='skip')
                .dropna(axis=1, how='all')
                .reset_index(drop=True))
        self.raw = df

        # 2. 保存起始时间，并准备数据
        self.start_time = pd.to_datetime(start_time)
        self.data = self._prepare_data(df)

        # 3. 构建插值器
        self.interps: dict[int, tuple[interp1d, float]] = {}
        self._build_interpolators()

        # 子流域映射水文站名字典
        self.id_2_name_dic = {
            818: '青阳岔',
            821: '双井河',
            830: '蚂蚁河',
            836: '槐树岔',
            839: '高家坪',
            844: '砖庙沟',
            869: '李家河',
            873: '小河沟',
            879: '三川沟',
            891: '驼耳巷沟',
            894: '周家圪崂河',
            900: '绥德',
        }

        # 控制断面对应坐标
        self.name_2_pos_dic = {
            '双井河': [362257.05709999986, 4151728.9606999997],
            '蚂蚁河': [368870.87490000017, 4157872.0755000003],
            '槐树岔': [380854.84979999997, 4159199.6592999995],
            '高家坪': [384366.29250000045, 4160094.9023000002],
            '砖庙沟': [396629.15969999973, 4163008.4471000005],
            '小理河': [398877.3167000003, 4163223.6567000002],
            '李家河': [398877.3167000003, 4163223.6567000002],
            '岔巴沟': [411224.80950000044, 4166724.201199999],
            '三川沟': [411224.80950000044, 4166724.201199999],
            '驼耳巷沟': [416866.97009999957, 4160591.9628999997],
            '周家圪崂河': [417026.16729999986, 4160444.7718000002],
            '小河沟': [405261.9676000001, 4164238.8126999997],
            '青阳岔': [362132.1705, 4151421.0489],

        }

    def _prepare_data(self, df: pd.DataFrame) -> pd.DataFrame:
        # 累计小时字段
        df['时'] = df.groupby(['年','月','日','子流域']).cumcount()
        # 构造 datetime 索引
        df['datetime'] = pd.to_datetime({
            'year':  df['年'],
            'month': df['月'],
            'day':   df['日'],
            'hour':  df['时']
        })
        df.set_index('datetime', inplace=True)
        df.sort_index(inplace=True)

        # 过滤掉 start_time 之前的数据
        df = df[df.index >= self.start_time]

        # 计算 sec_from_start = datetime - start_time
        out = []
        for sid, grp in df.groupby('子流域'):
            secs = (grp.index - self.start_time).total_seconds()
            tmp = pd.DataFrame({
                '子流域': grp['子流域'].values,
                '小时流量': grp['小时流量'].values,
                'sec_from_start': secs
            })
            out.append(tmp)
        result = pd.concat(out, ignore_index=True)
        result.set_index('sec_from_start', inplace=True)
        return result

    def _build_interpolators(self,
                             kind: str = 'quadratic',
                             fill_value: str = 'extrapolate'):
        """
        kind: 插值方式，可选值包括
           'linear'       — 线性插值
           'nearest'      — 最近邻插值
           'zero'         — 0 阶保持
           'slinear'      — 1 阶样条（同 linear）
           'quadratic'    — 2 阶样条
           'cubic'        — 3 阶样条
        """
        # 为每个子流域构造插值函数
        for sid, grp in self.data.groupby('子流域'):
            secs = grp.index.values
            flows = grp['小时流量'].values
            f = interp1d(secs, flows,
                         kind=kind,
                         fill_value=fill_value,
                         bounds_error=False)
            # 缓存：(interp1d 对象, 起始秒数 0)
            self.interps[sid] = (f, 0.0)

    def query(self, sid: int, sec: float) -> float:
        """
        按 sub-basin 与秒数查询流量。
        :param sid: 子流域 ID
        :param sec: 自 start_time 起的秒数
        :return: 插值流量
        """
        if sid not in self.interps:
            raise KeyError(f"No interpolator for sub-basin {sid}")
        f, t0 = self.interps[sid]
        return float(f(sec))

    def Update_side_inflow(self, station_id_list, River):
        t = River.current_sim_time
        for id in station_id_list:
            q = self.query(id, t)
            name = self.id_2_name_dic[id]
            pos = self.name_2_pos_dic[name]
            River.set_side_inflow(pos, q)
        pass

# 使用示例
if __name__ == '__main__':
    inflow = BatchInflow('case_test/大理河726数据.txt', '2017-07-25 04:00')

    for id in inflow.id_2_name_dic:
        try:
            name = inflow.id_2_name_dic[id]
            pos = inflow.name_2_pos_dic[name]
        except Exception as e:
            print(name, '无坐标')