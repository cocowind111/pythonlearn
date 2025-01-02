from multiprocessing import Process
#全局变量在进程中 不能共享
num = 10
def run():
    print("我是子进程的开始")
    global num
    num+=1
    print(num)
    print("我是子进程的结束")
if __name__=="__main__":
    p = Process(target=run)
    p.start()
    p.join()

    print(num)
