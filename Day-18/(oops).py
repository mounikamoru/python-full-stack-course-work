class Flipkart:
    #Class attribute
    discount = 10

    @classmethod
    #class method work with class attribute using cls instead of self 
    def updateDiscount(cls,new_discount):
        cls.discount=new_discount

    @staticmethod
    def welcome():
        print("Welcome to the flipkart")
    #instance method
    def myorders(self,order_id):
        #Instance attribute
        self.order_id=order_id
        print(f"You have order these product with id:{self.order_id}")

anju = Flipkart()
himaja = Flipkart()

print(anju.discount)
print(Flipkart.discount)

anju.myorders(1)

print(anju.order_id)

anju.updateDiscount(20)

anju.myorders(2)
anju.welcome()

Flipkart.updateDiscount(20)
Flipkart.welcome()

#1.creating e-comm product class
class E_comm:
    name = 'phone'
    price = 50000
    order_id = 212

    def display(self):
        print(f'{self.name},{self.price},{self.order_id}')

products = E_comm()
products.display()
print("-------------------")

#2.creating objects

products = E_comm()
products.display()
print("-------------------")


#3.Modifying Attributes

products.name = 'laptop'
products.price = 75000
products.order_id = 712

products.display()
print("-------------------")


#4.Instance Attributes

class Product:
    def __init__(self,name,price,order_id):
        #instance attribute
        self.name = name
        self.price = price
        self.order_id = order_id

# Creating two different product instances
p1 = Product("pods",2000,8)
p2 = Product("harddisk",7000,10)

print(p1.name)
print(p2.name)
print("-------------------")


#5.Class Attributes

class Product:
    #class attribute
    discount = 25

    #accessing class attribute
print(Product.discount)
print("-------------------")


#6.Adding a Method

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display():
        print(f'{self.name} , {self.price}, {self.quantity}')

    def cal_total_price(self):
        cal_total_price = self.price * self.quantity
        return cal_total_price

p1 = Product("TV", 40000, 3)
print(p1.cal_total_price())
print("-------------------")


#7.Instance Methods

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def apply_discount(self,discount):
        self.price = self.price * (discount/100)

p1 = Product("TV",50000,)
p1.apply_discount(10)
print(p1.price)
print("-------------------")

#8.Class Methods

class Product:
    discount = 10 #class attribute

    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount #modifies class attribute

Product.set_discount(15)
print(Product.discount)

#9.Static method

class Product:

    @staticmethod
    def welcome():
        print("welcome to new launches")
        
Product.welcome()








































