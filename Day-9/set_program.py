'''password = input("enter the password: ")
check=set()
if len(password)>8:
    for i in password:
        if i.islower():
           check.add('l')
        elif i.isupper():
            check.add('u')
        elif i.isdigit():
            check.add('n')
        else:
            check.add('s')
            if len(check)==4:
                print("strong password")
            else:
                print("weak password")
else:
    print("weak password")
'''

data={
      {'mounika':'status':True,'python':99,'mysql':90,'django':97},
      {'kavya':'status':True,'python':70,'mysql':60,'django':50},
      {'jahanavi':'status':True,'python':65,'mysql':56,'django':75},
      {'himaja':'status':True,'python':50,'mysql':90,'django':85},
      {'deepak':'status':False,'python':45,'mysql':40,'django':35}
     }
name = input("enter the student name:")
if name in data:
    if data[name]['status']:
        sum=data[name]['python']+ data[name]['my sql']+data[name]['django']
        avg=sum/3
        if avg>=90:
            print(f'congrats{name},you got first class')
        elif avg>=75:
            print(f'good{name}, wish you all the best for next time')
        elif avg>=60:
            print(f'{name},need improvement')
    else:
        print(f'{name},you failed in the exam bring your parents')
        
else:
    print(f'{name} data is not found')

        
    
