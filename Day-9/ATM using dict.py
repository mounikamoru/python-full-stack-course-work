#dict is mutable(same mem allocation,reference)
'''update,
keys need to be unique
keys needs to be immutable
keys can be string,int,float
values can be anything
dict is heterogenous
no indexing
dict is declared by curly braces only
s = set() -> declaration of set
d = dict() for set s = set()
go with [' ']
using the keys we are going to access the data
mutable-> list,set,dict
update-> 1.access 2. then add
items are going to give u tuple of key value pair
sorted will only care about keys
one key pair to add -> data['key']='value'
multiple -> use update data['key1','key2']='value'
to del
del data['key']
to pop
data.popitem-> dels the last key value pair from the dict
to del certain key -> data.pop('key')
to clear the key and values from the dict use data.clear()'''
data = {
    '123456':{'pin':'1234','balance':4000,'history':[]},
    '223456':{'pin':'1234','balance':5000,'history':[]},
    '333456':{'pin':'1234','balance':6000,'history':[]},
    '444456':{'pin':'1234','balance':7000,'history':[]},
    }
def deposit(acc_num):
    amount = int(input("enter the amount:"))
    data[acc_num]['balance']+=amount
    print(f"{amount} is deposited successfully")
    check_balance(acc_num)
    data[acc_num]['history'].append(f"{amount} is deposited")
def withdraw(acc_num):
    amount = int(input("Enter the amount:"))
    if data[acc_num]['balance'] >= amount:
        data[acc_num]['balance']-=amount
        print(f"{amount} is withdraw successfully")
        check_balance(acc_num)
        data[acc_num]['history'].append(f"{amount} is withdraw")
    else:
        print("Insuffient balance")
def change_pin(acc_num):
    old_pin = input("enter your old pin:")
    if old_pin == data[acc_num]['pin']:
        new_pin = input("enter the new pin")
        data[acc_num]['pin'] = new_pin
    else:
        print("Incorrect pin")
    

def check_balance(acc_num):
    print(f"current Balance: {data[acc_num]['balance']}")
def view_transaction(acc_num):
    if data[acc_num]['history']:
        print("-----------Transaction History----------------")
        for i in data[acc_num]['history']:
            print(i)
        else:
            print("-----------end of the transactions-------")
    else:
        print("No Transaction")
def menu():
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transaction")
    print("Change [P]in")
    print("[E]xit")
    

print("-------------welcome to the ATM-------------------")
acc_num = input("Enter the account number:")
pin = input("Enter the pin:")

if acc_num in data and data[acc_num]['pin']==pin:
    print("Login Successful")
    while True:
        menu()
        ch = input("Enteryour choice: ").lower()
        if ch =='c':
            check_balance(acc_num)
        elif ch == 'd':
            deposit(acc_num)
        elif ch =='w':
            withdraw(acc_num)
        elif ch == 'v':
            view_transaction(acc_num)
        elif ch == 'p':
            change_pin(acc_num)
        elif ch == 'e':
            print("--------------Thank you------------------")
            break
        else:
            print("Enter the valid choice")
else:
    print("Invalid Login")
