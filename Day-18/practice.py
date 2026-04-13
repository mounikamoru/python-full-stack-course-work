
#1.Book Details Display

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f'Title: {self.title}, Author: {self.author}, Price: {self.price}')

b1 = Book("wish i could tell you", "name", 500)
b2 = Book("the girl in the room number 105", "name", 300)
b1.display()
b2.display()


#2.Employee Salary Calculator

class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_annual_salary(self):
        return self.base_salary*12

e1 = Employee("anju",50000)
e2 = Employee("sree",60000)
print(e1.calculate_annual_salary())
print(e2.calculate_annual_salary())


#3.Student Grade Evaluator

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)

    def result(self):
        if self.average() > 35:
            return "Pass"
        else:
            return "Fail"

s1 = Student("anju",[85,78,99])
s2 = Student("sree",[88,90,91])
print(s1.average())
print(s1.result())
print(s2.average())
print(s2.result())

#4.Bank Account Simulation

class BankAccount:
    def __init__(self,acc_name):
        self.acc_name = acc_name
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient")
    def display(self):
        print(f'bal: {self.balance}')
    

a1 = BankAccount('anju')
a1.deposit(10000)
a1.withdraw(5000)
a1.display()

#5.Create a Car class with method to update and show odometer after driving.

class Car:
    def __init__(self,car_name):
        self.car_name = car_name
        self.odometer = 0

    def add_distance(self, km):
        self.odometer += km

    def display(self):
        print(f'{self.car_name} has travelled {self.odometer} kms')

c1 = Car('swift')
c2 = Car("BMW")

c1.add_distance(200)
c2.add_distance(500)

c1.display()
c2.display()

#6.Create a Movie class with method to check if movie is suitable for kids.

class Movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating
    def is_children_friendly(self):
        if self.rating >8:
            print("movie can be watched by childern")
        else:
            print("no")
m1 = Movie('the croods', 9)
m2 = Movie('animation',5)
m1.is_children_friendly()
m2.is_children_friendly()

#7.Create Product class with discount application logic.

class Product:
    def __init__(self,p_name,price):
        self.p_name = p_name
        self.price = price
    def apply_discount(self,discount):
        self.discount = discount
        self.price -= self.price * (self.discount/100)
    def display(self):
        print(f'{self.p_name} is available for {self.price} after discount')
p1 = Product('laptop',50000)
p1.apply_discount(10)
p1.display()
 
#8.Create a class to convert Celsius to Fahrenheit and vice versa.

class Conversion_of_Celsius_to_Fahrenheit:
    def __init__(self,Celsius,Fahrenheit):
        self.Celsius = Celsius
        self.Fahrenheit = Fahrenheit
    def Celsius_to_Fahrenheit(self):
        self.Fahrenheit = (self.Celsius *9/5) + 32
    def Fahrenheit_to_Celsius(self):
        self.Celsius = (self.Fahrenheit - 32) * 5/9
    def display(self):
        print(f'for entered {self.Celsius} the Fahrenheit value is {self.Fahrenheit}')
        print(f'for entered {self.Fahrenheit} the Fahrenheit value is {self.Celsius}')

c1 = Conversion_of_Celsius_to_Fahrenheit(78,99)
c1.Celsius_to_Fahrenheit()
c1.display()

c2 = Conversion_of_Celsius_to_Fahrenheit(78,99)
c2.Fahrenheit_to_Celsius()
c2.display()

#9.

class YouTubeChannel1:
    def __init__(self,channel_name,subscribers,total_views):
        self.channel_name = channel_name
        self.subscribers = subscribers
        self.total_views = total_views
    def upload_viedo(self,views):
        self.views = views
        self.total_views += self.views
    def gain_subscribers(self,count):
        self.count = count
        self.subscribers += self.count
    def display_stats(self):
        print(f'Channel: {self.channel_name} \nSubscribers: {self.subscribers} \nTotal Views: {self.total_views}')

user = YouTubeChannel1("tech_world",1000,5000)
user.upload_viedo(200)
user.gain_subscribers(150)
user.display_stats()

        
        
        
