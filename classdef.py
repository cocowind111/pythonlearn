class gagadenvyou:
    def __init__(self,name,age):
        self.name= name 
        self.age = age 
    def __str__(self):
        return f"{self.name},{self.age}"
print("hello")
print(__name__)
if __name__=="__main__":
    print(gagadenvyou)