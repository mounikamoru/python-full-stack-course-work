'''
polymerphism-same method different action

method-1(overloading)same methods, different parameters, same/diff class
we dont have method overloading, it is not supported my python
method-2(overidding)same methods, same parameters, parent/child concept
one method in parent class one method in the child class
rewriting the method again in child class
'''

class Hotstar:
    def __init__(self,username):
        print(f'Hi {username}!\nWelcome to the hotstar')
    def promo(self):
        print("You can watch promo")
    def login(self):
        print("You can login to the hotstar")
    def search(self):
        print("You can search the movies")
    def profile(self):
        print("you can edit your profile")
    def viedocontroller(self):
        print("you can play and pause")
    def suggestions(self):
        print("you can check out suggestions")

    def movie(self):
        print("you have access to old movies only")
    def ads(self):
        print("ads will run")
    def download(self):
        print("you cant download the movie")
    def viedoquality(self):
        print("you will get low quality ")
hima = Hotstar("himaja")
hima.promo()
hima.login()
hima.search()
hima.profile()
hima.viedocontroller()
hima.suggestions()
hima.movie()
hima.ads()
hima.download()
hima.viedoquality()

class PremiumHotstar(Hotstar):
    def __init__(self,username):
        print(f'Hi {username} welcome to premium hotstar')
    def movie(self):
        print("you have access to all movies")
    def ads(self):
        print("ads will skip")
    def download(self):
        print("you can download the movie")
    def viedoquality(self):
        print("you will get high quality ")

anju = PremiumHotstar("anju")
anju.promo()
anju.login()
anju.search()
anju.profile()
anju.viedocontroller()
anju.suggestions()
anju.movie()
anju.ads()
anju.download()
anju.viedoquality()

              
operater over_ridding:

class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num+other.num
    def __sub__(self,other):
        return self.num-other.num
    def __mul__(self,other):
        return self.num*other.num
    def __gt__(self,other):
        return self.num>other.num
    def __lt__(self,other):
        return self.num<other.num
    def __str__(self):
        return str(self.num)

a = number(10)
b = number(20)

print(a+b)
print(a-b)
print(a*b)
print(a>b)
print(a<b)
print(a+b)
