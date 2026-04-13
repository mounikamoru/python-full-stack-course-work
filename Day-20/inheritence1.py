
#single inheritence-extract the properties from parent class to child class

class InstagramV1:
    def reel(self):
        print("You can post the reel")

class InstagramV2(InstagramV1):
    def story(self):
        print("You can update the story")

        

#before extracting the features from parent class
print("Anju - Instagram")
anju = InstagramV1()
anju.reel()

#after extracting the features from parent class
print("Himaja - Instagram")
himaja = InstagramV2()
himaja.reel()
himaja.story()

#----------------------------------------------------------------

#multi-level inheritance
#parent to child
#child to grand child

class InstagramV1:
    def reel(self):
        print("You can post the reel")

class InstagramV2(InstagramV1):
    def story(self):
        print("You can update the story")


class InstagramV3(InstagramV2):
    def note(self):
        print("You can add the your thoughts")
        

print("Anju - Instagram")
anju = InstagramV1()
anju.reel()

print("Himaja - Instagram")
himaja = InstagramV2()
himaja.reel()
himaja.story()

print("Keerthi - Instagram")
keerthi = InstagramV3()
keerthi.reel()
keerthi.story()
keerthi.note()

#multiple level inheritence - can have more than two parent classes or can extract features from more than two parent clasess to single child class


class InstagramV1:
    def note(self):
        print("You can add the your thoughts")

class meta:
    def ai(self):
        print("you can use ai")

class crossplatform:
    def integrating(self):
        print("you can integrate with whatsapp and facebook")

class InstagramV4(meta,crossplatform,InstagramV1):
    def repost(self):
        print("you can repost the post")


print("Keerthi - Instagram")
keerthi = InstagramV1()
keerthi.note()

print("Prasanna - Instagram")
prasanna = InstagramV4()
prasanna.note()
prasanna.ai()
prasanna.integrating()
prasanna.repost()


#hybrid inheritence - combination of any two or more inheritance

class InstagramV1:
    def reel(self):
        print("You can post the reel")

class InstagramV2(InstagramV1):
    def story(self):
        print("You can update the story")


class InstagramV3(InstagramV2):
    def note(self):
        print("You can add the your thoughts")

class meta:
    def ai(self):
        print("you can use ai")

class crossplatform:
    def integrating(self):
        print("you can integrate with whatsapp and facebook")

class InstagramV4(meta,crossplatform,InstagramV3):
    def repost(self):
        print("you can repost the post")

print("Anju - Instagram")
anju = InstagramV1()
anju.reel()

print("Himaja - Instagram")
himaja = InstagramV2()
himaja.reel()
himaja.story()

print("Keerthi - Instagram")
keerthi = InstagramV3()
keerthi.reel()
keerthi.story()
keerthi.note()

print("Prasanna - Instagram")
prasanna = InstagramV4()
prasanna.reel()
prasanna.story()
prasanna.note()
prasanna.repost()



#hieracy-single parent multiple childs


class InstagramV1:
    def reel(self):
        print("You can post the reel")

class InstagramV2(InstagramV1):
    def story(self):
        print("You can update the story")

#from here
class InstagramV3(InstagramV2):
    def note(self):
        print("You can add the your thoughts")

class meta(InstagramV3):
    def ai(self):
        print("you can use ai")

class crossplatform(InstagramV3):
    def integrating(self):
        print("you can integrate with whatsapp and facebook")
#to here example for hieracy
        
class InstagramV4(meta,crossplatform,InstagramV3):
    def repost(self):
        print("you can repost the post")

print("Anju - Instagram")
anju = InstagramV1()
anju.reel()

print("Himaja - Instagram")
himaja = InstagramV2()
himaja.reel()
himaja.story()

print("Keerthi - Instagram")
keerthi = InstagramV3()
keerthi.reel()
keerthi.story()
keerthi.note()

print("Prasanna - Instagram")
prasanna = InstagramV4()
prasanna.reel()
prasanna.story()
prasanna.note()
prasanna.repost()

class A:
class B(A):

class A:
class B(A):
class c(B):

class A:
class B:
class C:
class D(A,B,C):

class A:
class B(A):
class C(A):
class D(A):

#if two methods have same name
#example of single inheritence
class WhatsappV0:
    def status(self):
        print("you can upload the images")

class WhatsappV1(WhatsappV0):
    def status(self):
        super().status() #if 
        print("You can like react and reply")
    
anju = WhatsappV1()
anju.status()

#if three methods have same name
#this is also example for multi level inheritance
class WhatsappV0:
    def status(self):
        print("you can upload the images")

class WhatsappV1(WhatsappV0):
    def status(self):
        super().status() 
        print("You can like react and reply")

class WhatsappV2(WhatsappV1):
    def status(self):
        super().status() 
        print("You can add music and filter also")
    
anju = WhatsappV2()
anju.status()

#multiple
class WhatsappV0:
    def status(self):
        print("you can upload the images")

class WhatsappV1:
    def status(self):
        print("You can like react and reply")

class WhatsappV2(WhatsappV0,WhatsappV1):
    def status(self):
        WhatsappV0.status(self)
        WhatsappV1.status(self)
        print("You can add music and filter also")
    
anju = WhatsappV2()
anju.status()

