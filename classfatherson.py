class gagadenvyou:
    def __init__(self,name,age):
        self.name= name 
        self.age = age 
    def __str__(self):
        return f"{self.name},{self.age}"
    def sense2gaga(self):
        print("gagadenvyou")

class gagadelaopo(gagadenvyou):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.yeyebaby='littleyeye'
    def baby(self):
        print(str(self.yeyebaby))
    def sense2gaga(self):
        print("gagadelaopo")

yeye=gagadelaopo("yy",18)
yeye2=gagadenvyou("yy",18)
print(yeye.name)
print(yeye)
yeye.baby()
yeye2.sense2gaga()