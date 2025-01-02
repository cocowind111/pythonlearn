from multiprocessing import Pool
import time

def worker(x):
    time.sleep(2)
    return x * x

if __name__ == "__main__":
    time_start=time.time()
    pool = Pool(processes=4)

    # 提交任务
    results = pool.map(worker, [1, 2, 3, 4, 5])

    # 关闭进程池，不再接受新的任务
    pool.close()

    # 等待进程池中的所有任务执行完毕
    pool.join()

    print(results)
    time_end=time.time()
    print(f'共耗费{time_end-time_start}秒用于计算')