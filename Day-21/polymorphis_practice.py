
#1.
class Payment:
    def pay(self, amount):
        pass

class Creditcard(Payment):
    def pay(self,amount):
        print("payment is done with the Creditcard")

class Paypal(Payment):
    def pay(self,amount):
        print("payment is done with the Paypal")

def check_out(payment_method):
    payment_method.pay(250)


check_out(Paypal())

#2.

class Printer:
    def operate(self):
        print("printing a file")

class InkjetPrinter(Printer):
    def operate(self):
        print("printing a pdf")

class LaserPrinter(Printer):
    def operate(self):
        print("printing a picture")

def printout(printingmethod):
    printingmethod.operate()

printout.InkjetPrinter()

printout.LaserPrinter()

#4.



class Video:
    def play(self):
        print("Playing Video")
class ShortVideo(Video):
    def play(self):
        print("Playing short video")
class LiveStream(Video):
    def play(self):
        print("Streaming live now")

o1 = Video()
o2 = ShortVideo()
o3 = LiveStream()
o1.play()
o2.play()
o3.play()







































'''
Different Payment Methods

Create a class Payment with a method to process payment.
Create subclasses CreditCard and PayPal that
implement the payment method differently.
Create a function to perform checkout using different payment
methods and process a payment of 250.

class Payment:
    def display(self,amount):
        self.pay = pay
        print("payment is processing")

class CreditCard(Payment):
    def display(self,amount):
        print("payment through phnpay")

class PayPal(Payment):
    def display(self,amount):
        print("payment through gpay")
def 
p1 = PayPal(250)
p1.display()

'''