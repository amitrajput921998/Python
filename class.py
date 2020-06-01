# Creating class

class Person:
    def __init__(self,first_name,last_name,age):
        self.person_first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person("Amit","Singh",21)
print(p1.person_first_name)


class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.laptop_brand_name=brand_name
        self.model_name=model_name
        self.price=price

p3=Laptop("hp","ideapad",45000)
p4=Laptop("del","oera",30000)
print(p3.laptop_brand_name)
print(p3.model_name)
print(p3.price)
        
