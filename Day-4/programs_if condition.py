min_balance=5000
cur_balance=2000

if cur_balance<min_balance:
    print("send message and cut some amount")

min_charge =20
cur_charge =15

if cur_charge< min_charge:
    print("send alert to charge the phone")


data =('user@gmail.com','user@123')
mail =input("enter the email:")
password= input("enter the password:")

if data ==(mail,password):
     print("login successful")
else:
    print("invalid login")


fruits = ['mango','apple','papaya','pine apple']
search_item= input("search here: ")

if search_item in fruits:
    print(f"{search_item} found! Buy Now")
else:
    print(f'{search_item} is out of stock , we will notify you once it is available')


time = int(input("enter the hour:"))

print("Available buses are: ")
if 0 <= time <=6 :
    print("Bus2\nBus7\nBus10\nBus14")
elif 7<= time <=12:
    print("Bus1\nBus19\nBus14")
elif 18<= time<=24:
    print("Bu90\nBus80\nBus70")
else:
    print("enter the time in the given range")



print("welcome to uber, Book your ride")

print("1.Bike")
print("2.auto")
print("3.cab")

choice =int(input("choose the option:"))
if choice == 1:
    print("Hey,you have booked bike successfully.\nDriver is on the way. wear the seat belt")
elif choice ==2:
    print("hello, you have booked auto successfully. \nDriver is on the way")
elif choice ==3:
    print("hello , you have booked the cab successfully")


login_status = False
premium_account = True

if login_status:
    print("welcome to the Hotstar")
    if premium_account:
        print("play the video with the high quality and without adds")
    else:
        print("play the video with normal quality and with adds")
else:
    print("invalid login")
