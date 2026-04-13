
#constructor

'''
__init__ constructors is a special method it is automatically called the
moment when object is created

with the help of self we are able to call the objects(anju,himaja)'''

class instagram:
    def __init__(self,username,password):
        self.username=username #insta attr(username)
        self.password=password
        print(f'Hello {self.username}, Welcome to instagram')


anju = instagram('anjusree','anju@123')
himaja= instagram('himaja','himaja@123')

'''
encapsulation - restricting the information
username-public
pass-private,password is private it can be accessed inside the function only,use function called get_password
post-protected
'''
class instagram:
    def __init__(self,username,password):
        self.username=username 
        self.__password=password
        self._posts=[]
        self.__email=email

    @property # is a decorator, myposts is variable,accessing protected

    def myposts(self):
        return self._posts

    @myposts.setter
    def myposts(self,postname):
        self._posts.append(postname)
    

    
    #how to access private
    def get_password(self): #get n set password are functions
        return self.__password

    #to change the private

    def set_password(self,new_password):
        self.__password=new_password

    def get_email(self):
        return self.__email

    def set_email(self,new_email):
        self.__email=new_email
        
#username can be accessed inside outside
anju = instagram('anjusree','anju@123')

print("Before updating:",anju.username)
anju.username='himaja'
print("After updating:",anju.username)

print("before updating:",anju.get_password())
anju.__password = 'himaja@123'
print("After updating:",anju.__password)

print(anju.myposts)
anju.myposts='sunset.png'
anju.myposts='beach.mp4'
print(anju.myposts)

print("before updating:",anju.get_email())
anju.__password = 'himaja@gmail.com'
print("After updating:",anju.__email())
