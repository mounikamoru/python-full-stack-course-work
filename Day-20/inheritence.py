
#1.Vehicle and Car Inheritance

#using super class
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f'{self.brand} vehicle started')

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def show_info(self):
        print(f'brand: {self.brand} and model : {self.model} of the car')

c1 = Car('Camry',"v2")
c1.start()

c2 = Car("swift","v3")
c2.show_info()

#without using super class
class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f'{self.brand} vehicle started')

class Car(Vehicle):
    def car_model(self,model):
        self.model = model
    def show_info(self):
        print(f'Brand: {self.brand} and Model: {self.model} of the car')

c1 = Vehicle('Camry')
c1.start()

c2 = Car("swift")
c2.car_model("v3")
c2.show_info()


#2.Account and SavingsAccount

Create a class Account with a method to store and display balance.
Create a subclass SavingsAccount that adds interest to the balance.
Create an object with balance 1000 and interest rate 5%, add interest, and display the updated balance.


class Account:
    def __init__(self,bal):
        self.bal = bal

    def store_bal(self):
        print(f'balance: {self.bal}')


class SavingsAccount(Account):
    def add_interest(self,interest):
        self.interest = interest
        self.bal = self.bal + (interest/100)
        print(self.bal)

a1 = SavingsAccount('anju',1000)
a1.add_interest(5)

class Account:
    def __init__(self,bal):
        self.bal = bal
        
    def store_bal(self):
        print(f'balance: {self.bal}')

    

class SavingsAccount(Account):
    def __init__(self,bal,interest):
        super().__init__(bal)
        self.interest = interest
    def after_interest_bal(self):
        self.bal = self.bal + (self.interest/100)
        print(self.bal)

a1 = SavingsAccount(1000,5)
a1.store_bal()
a1.after_interest_bal()

#3.User and Admin Access

Create a class User with a method to display user access.
Create a subclass Admin that overrides the method to display admin access.
Create an object with username "admin_john" and display the access level.


class User:
    def __init__(self,username):
        self.username = username

    def access(self):
        print(f'{self.username} has user access')

class Admin(User):
    def access(self):
        print(f'{self.username} has admin access')

u1 = Admin("admin_john")
u1.access()
        

#4.Employee Role Display

Create a class Employee with a method to display a general role.
Create a subclass Manager that overrides the method to display a
manager’s role.
Create an object with name "Ravi" and display the role.


class Employee:
    def __init__(self,name):
        self.name = name
    def display(self):
        print(f'{self.name} employee is at general role')

class Manager(Employee):
    def display(self):
        print(f'{self.name} employee is at manager role')
                 
    
e1 = Manager("Ravi")
e1.display()

#5.Rectangle with Color and Area

Create a class Shape with a method to display color.
Create a subclass Rectangle that stores length and width and calculates area.
Create an object with color "Blue", length 4, and width 5,
then display the color and area.


class Shape:
    def __init__(self,colour):
        self.colour = colour
    def display_colour(self):
        print(f'shape has colour {self.colour}')

class Rectangle(Shape):
    def __init__(self,colour,length,wid):
        super().__init__(colour)
        self.length = length
        self.wid =wid
    def area(self):
        return self.length * self.wid
        

s1 = Rectangle("blue", 4, 5)
s1.display_colour()
print("area: ",s1.area())



#6.Appliance and Washing Machine

Create a class Appliance to store the brand.
Create a subclass WashingMachine with a method to display a washing_action.
Create an object with brand "LG" and display the washing action.

class Appliance:
    def __init__(self,brand):
        self.brand = brand

    def display(self):
        print(f' Appliance brand is {self.brand}')

class WashingMachine(Appliance):
    def washing_action(self):
        print(f'{self.brand} washing cloths')

a1 = WashingMachine("LG")
a1.display()
a1.washing_action()
        
#7.Member and Premium Member

Create a class Member with a method to show basic benefits.
Create a subclass PremiumMember that overrides the method to
show premium benefits.
Create an object with name "Akash" and display the benefits.   
    

#8.Vehicle and Bike

Create a class Vehicle with a method to display driving action.
Create a subclass Bike with a method to display the number of wheels.
Create an object and call both methods.

#9.Teacher and Subject Teacher

Create a class Teacher with a method to display general teaching.
Create a subclass MathTeacher that overrides the method to
display subject-specific teaching.
Create an object with name "Mrs. Kapoor" and display the teaching role.

#10.Device and Laptop

Create a class Device with a method to display power status.
Create a subclass Laptop with a method to open an IDE.
Create an object and call both methods.












class Account:
    def __init__(self,balance):
        self.balance = balance

    def show_balance():
        print(f'Account_balance:{balance}')

class Savings_Account(Account):
    def __init__(self,interest_rate):
        super()._init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self,new_balance):
       
  

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def display_user(self):
        print(f'Username: {self.username} \nEmail: {self.email}')
class Creator(User):
    def __init__(self,username, email,channel_name,subscribers):
        User.__init__(self,username, email)
        self.channel_name = channel_name
        self.subscribers = subscribers
    def display_Creator(self):
        print(f'Channel: {self.channel_name} \nSubscribers: {self.subscribers}')

User1 = User('john_doe','john@email.com')
User1.display_user()

User2 = Creator('john_doe','john@email.com','JohnVlogs', 2000)
User2.display_Creator()


class Creator:
    def __init__(self,name,subscribers):
        self.name = name
        self.subscribers = subscribers

class PremiumCreator(Creator):
    def __init__(self,name,subscribers,membership_fee):
        super().__init__(name,subscribers)
        self.subscribers = subscribers
        self.membership_fee = membership_fee
    def display(self):
        print(f'Name: {self.name} \nSubscribes: {self.subscribers} \nMembership:{self.membership_fee}')

creator1 = PremiumCreator('Alice', 5000, 299)
creator1.display()



































