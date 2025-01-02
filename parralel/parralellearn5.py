from multiprocessing import Process,pool
import multiprocessing
#全局变量在进程中 不能共享
mylist = []
def run():
    print("我是子进程的开始")
    global mylist
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist)
    print("我是子进程的结束")

if __name__=="__main__":
    p = Process(target=run)
    pooltest=pool()
    p.start()
    p.join()

    print(mylist)
print('CPU number:' + str(multiprocessing.cpu_count()))