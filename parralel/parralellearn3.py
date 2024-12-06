import time 
import multiprocessing

def saykw(name,**kwargs):
    print(f'我想说的话是{name}')
    for name1 in kwargs.items():
        print(f'我想说的话是{name1}')
def say(name,*args):
    print(f'我想说的话是{name}')
    for name1 in args:
        print(f'我想说的话是{name1}')        
name1='yeye'
name2='gaga'
if __name__ == '__main__':
    time_start=time.time()
    say_process=multiprocessing.Process(target=say,args=(name1,name2,name2))
    saykw_process=multiprocessing.Process(target=saykw,kwargs={'name':'gaga','name2':'yeye','name3':'yeyedebaby'})
    saykw_process2=multiprocessing.Process(target=saykw,args=(name1,),kwargs={'name2':'yeye','name3':'yeyedebaby'})
    say_process.start()
    saykw_process2.start()
    say_process.join()

    saykw_process.start()
    saykw_process.join()

    time_end=time.time()
    print(f'共耗费{time_end-time_start}秒用于计算')