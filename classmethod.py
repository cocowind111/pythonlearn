class gagadenvyou:
    class_attribute='person'
    def __init__(self,name,age):
        self.name= name 
        self.age = age 
    def __str__(self):#实例方法
        return f"{self.name},{self.age}"
    @classmethod
    def classmethodtest(cls):#类方法
        print(cls.class_attribute)
    @staticmethod
    def staticmethod(a,b):#静态方法
        return a+b
obj=gagadenvyou('yeyepig','18')
print(obj)
print(obj)
print(gagadenvyou.classmethodtest)
print(obj.classmethodtest)
c=gagadenvyou.staticmethod(1,2)
print(c)
d=obj.staticmethod(1,2)
print(d)
a=1
print(f'a的值为{a}')
