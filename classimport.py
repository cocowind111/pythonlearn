from classdef import gagadenvyou
import classdef
gaga= gagadenvyou('yeye',18)
gaga1=classdef.gagadenvyou('yeye',18)
if __name__=="__main__": #只有这个py文件作为主程序执行时，才会调用这个if语句下面的代码。如果是模块被调用的话则不会执行。
    print(gaga)
    print(gaga.name)
    print(gaga1)
    print(gaga1.name)

