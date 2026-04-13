Sprint('*' * 30)
print("CONDITIONAL STATEMENTS")
print('*' * 30)
print('---------------simple if--------------------')

#1.
recharge = 0
if recharge <= 0:
    print('recharge immediatly')

#2.
screen_shot = True
if screen_shot:
    print("screen_shot is taken")

#3.
button_pressed = True
if button_pressed:
    print("play viedo")

#4.
green_mark = True
if green_mark:
    print("Active in instagram")

#5.
double_tap = True
if double_tap:
    print('post gets a like')

#6.
button_click = False
if button_click:
    print('captures photos')

#7.
mesg_arrives = True
if mesg_arrives:
    print('shows notification')

#8.
battery = 20
if battery < 15:
    print('get charge')



print('-------------------if else---------------------')
#1.
like_item = input("Do you like the Myntra item? (yes/no): ")
if like_item == "yes":
    print("Keep the item.")
else:
    print("Return the item.")

#2.
turn = input("Did you take left or right? ")
if turn == "left":
    print("You are on the correct route.")
else:
    print("Wrong turn taken. Map will change the route.")

#3.
user = input("Do you have YT music premium? (yes/no): ")
if user == "yes":
    print("you can download songs")
else:
    print("upgrade to premium")

#4.
internet_speed = input("speed of your internet(high/low): ")
if internet_speed == "high":
    print("play video with high quality")
else:
    print("play video with low quality")

#5.
order_status = ["placed", "shipped", "in_transit", "out_for_delivery", "delivered"]

current_status = input("Enter current order status: ")

if current_status in order_status:
    print("Order status:", current_status)
else:
    print("Invalid order status")



print('-------------------elif---------------------')

#1.
cost = int(input("enter the cost of living:"))
if 10000 <= cost <= 20000:
    print("silver living")
elif 21000 <= cost <= 30000:
    print("gold living")
elif 31000 <= cost <= 40000:
    print("platinum living")

#2.
status_of_message = input("enter the tick status(single/double/blue tick:")
if status_of_message == "single":
    print("message sent")
elif status_of_message == "double":
    print("message delivered")
else:
    print("message read")

#3.
phone_mode = input("enter the state of the phone(silent/vibration/ringtone:")
if phone_mode == "silent":
    print("phone is on silent mode")
elif phone_mode == "vibration":
    print("phone is on vibration mode")
elif phone_mode == "ringtone":
    print("phone is ringing")

#4.
traffic = input("traffic type(low/medium/heavy):")
if traffic == "low":
    print("route line shows green colour")
elif traffic == "medium":
    print("route line shows orange colour")
else:
    print("route line shows red colour")


print('-------------------nested if---------------------')
#1
internet = True
receiver_available = True
if internet:
    if receiver_available:
        print("Message sent successfully.")
    else:
        print("Receiver not available.")
else:
    print("No internet connection.")
    
#2.
orders = ["ORD101", "ORD102", "ORD103"]
delivered_orders = ["ORD101"]
order_id = input("Enter order ID: ")
if order_id in orders:
    if order_id in delivered_orders:
        print("Order already delivered.")
    else:
        print("Order is in progress.")
else:
    print("Order not found.")
#3.
account_exists = True
balance = 500
withdraw_amount = 300
if account_exists:
    if balance >= withdraw_amount:
        print("Transaction successful.")
    else:
        print("Insufficient balance.")
else:
    print("Account not found.")
#4.
app_open = True
login_correct = False

if app_open:
    if login_correct:
        print("Instagram login successful.")
    else:
        print("Incorrect login details.")
else:
    print("App not opened.")
        
    

