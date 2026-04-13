


'''


#1.Private bank balance

Create a class Account with appropriate methods to:

store balance
deposit money
display the balance



class Account:
    def store_balance(self,name):
        self.name = name
        self.__balance = 0
    def deposit_money(self, amount):
        self.__balance += amount

    def display(self):
        print(f'account of {self.name} have balance {self.__balance}')
a1 = Account()
a1.store_balance('anju')
a1.deposit_money(1000)
a1.display()
        

#2.Password Protection


Create a class Account with a private password
and methods to verify it and display account details.


class Account:
    def __init__(self,acc_name,password):
        self.acc_name = acc_name
        self.__password = password

    def change_password(self,old,new):
        if old == self.__password:
            self.__password = new
            print("password changed")
        else:
            print("incorrect old password")
a1 = Account('anju','anju@123')
a1.change_password('anju@123','Anjusree@123')


#3.Encapsulated Student Info

Create a class Student with a private variable to store the student’s name.
Add a method to return the name.
Create an object with the name "Riya" and print the name.


class Student:
    def __init__(self,name):
        self.__name = name
    def name_of_student(self):
        return self.__name

s1 = Student('Riya')
print(s1.name_of_student())

#4.Employee Salary

Create a class Employee with a private variable to store the salary.
Add a method to return the salary.
Create an object with salary 40000 and print it.


class Employee:
    def __init__(self,e_name,salary):
        self.e_name = e_name
        self.__salary = salary
    def display_salary(self):
        return self.e_name, self.__salary
e1 = Employee('anju',50000)
print(e1.display_salary())

#5.Product Stock Management

Create a class Product with a private variable to store stock (initially 100).
Add a method to reduce stock when a product is bought and another method to check the remaining stock.
Create an object, buy 20 items, and display the remaining stock.



class Product:
    def __init__(self):
        self.__stock = 100

    def available_stock(self,p_brought):
        if p_brought <= self.__stock:
            self.__stock -= p_brought
        else:
            print("out of stock")
    def remain_stock(self):
        return self.__stock
p1 = Product()
p1.available_stock(20)
print(p1.remain_stock())

#get and set

def get_email(self):
    return self.__email
def set_email(self,new_email):
    self.__email = new_email

def get_pass(self):
    return self.__password
def set_pass(self,new_password):
    self.__password = new_password
 

'''

class YouTubeEarnings:
    def __init__(self,revenue):
        self.__revenue = revenue

    def set_revenue(self,amount):
        self.__revenue += amount

    def add_earnings(self,amount):
        self.__revenue += amount

    def get_revenue(self):
        print(self.__revenue)

user1 = YouTubeEarnings(0)
user1.set_revenue(1000)
user1.add_earnings(500)
user1.get_revenue()
            
















