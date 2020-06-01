class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price

x=Laptop('Lenova','Ideapad',40000)
y=Laptop('Dell','Metaball',32000)

print(x.brand_name,x.model_name,x.price)
print(y.brand_name,y.model_name,y.price)
