



class Employee : 


    def __init__(self,name,age):    #constructor   # used we need to assing the initial values 
        self.name = name
        self.age = age

    def display(self):
        print("hello first class")
        print(self.name)




emp1 = Employee("riyaz",1)   #object
emp1 = Employee("riyaz",1)

emp1.display()




class youtube : 


    def __init__(self,count):    #constructor   # used we need to assing the initial values 
        
        self.count = count

    def subcribe(self):
        print("subscribe successfully")


youtu1 = youtube(1)

youtu1.subcribe()
# pydantic library 
#pip install pydantic 

#most popular data validation and parsing library for Python.