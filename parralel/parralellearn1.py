import time 
def sing():
    for i in range(3):
        print('唱歌。。。。。')
        time.sleep(0.5)
def dance():
    for i in range(3):
        print("跳舞")
        time.sleep(0.5)
if __name__ == '__main__':
    time_start=time.time()
    sing()
    dance()
    time_end=time.time()
    print(f'共耗费{time_end-time_start}秒用于计算')