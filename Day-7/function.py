def function_name(arg):
    #stmts
    return


function_name(para)


def wish(name):
    print(f'Hello {name}, Welcome to "python 100 days of program"')


wish('swarna')
wish('manisha')
wish('tharun')
wish('aditya')
wish('bhuvan')

def display(username,email,password):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)
    


display('sudheer',' @gmail.com','s@123')
display('sudheer@gmail.com','sudheer','s@123')
display('s@123','sudheer@gmail.com','sudheer')


def display(username,email,password):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)
    

display(username='sudheer',email='sudheer@gmail.com',password='s@123')
display(email='sudheer@gmail.com',username='sudheer',password='s@123')
display(password='s@123',email='sudheer@gmail.com',username='sudheer')



def display(username,email,password='',phoneno='+91'):
    print("Username:",username)
    print("Email:",email)
    print("Password:",password)
    print("Phone no:",phoneno)
    

display('sudheer',' @gmail.com','s@123','1234567890')
display('sudheer',' @gmail.com')


def display(*names):
    print(names)

display('tharun','gowtham','bharath')
display('tharun','gowtham')
display('tharun')
'''
def display(**names):
    print(names)

display(n1='tharun',n2='gowtham',n3='bharath')
display(n1='tharun',n2='gowtham')
display(n1='tharun')










