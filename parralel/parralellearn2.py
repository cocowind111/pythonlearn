import time 
import multiprocessing
def sing(b):
    for i in range(3):
        print(f'唱歌with{b}')
        time.sleep(0.5)
def dance(name,sex,age):
    for i in range(3):
        print(f'跳舞with{name},性别为{sex},年龄为{age}')
        time.sleep(0.5)
def say(**kwargs):
    for i in range(3):
        print(f'我想说的话是{kwargs}')
name1='yeye'
name2='gaga'
sex='man'
age=18
if __name__ == '__main__':
    time_start=time.time()
    sing_process=multiprocessing.Process(target=sing,args=('yeye',))#位置参数
    dance_process=multiprocessing.Process(target=dance, args=(name2, sex , age))
    # dance_process=multiprocessing.Process(target=dance, kwargs={'name':name2,'sex':sex,'age':age})
    say_process=multiprocessing(target=say,kwargs='turtle')
    sing_process.start()
    dance_process.start()
    say_process.start()
    time_end=time.time()
    print(f'共耗费{time_end-time_start}秒用于计算')