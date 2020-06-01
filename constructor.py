'''class Car:
    brand="audi"
    money=250000;
    def Model(self):
        print("brand:%s\nMoney:%d"%(self.brand,self.money)

d = Car()
d.Model()

class Employee:  
    id = 10;  
    name = "John"  
    def display (self):  
emp = Employee()  
emp.display()  '''

class Student:
    def __init__(self,name,id,age):
     self.name=name
     self.id=id
     self.age=age

p1=Student("Amit",75,21)

print(p1.name)
print(getattr(p1,'name'))
setattr(p1,"age",23)
print(getattr(p1,"age"))
print(hasattr(p1,"id"))
print(p1.__dict__)
print(p1.__doc__)
print(p1.__module__)
      
    
    
