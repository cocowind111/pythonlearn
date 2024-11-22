class gagadenvyou:
    def __init__(self,name,age):
        self.name= name 
        self.age = age 
    def __str__(self):
        return f"{self.name},{self.age}"
b=gagadenvyou('yeye',18)
print(b.name)