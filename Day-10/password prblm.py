password = input ("enter your password:")
check = set()
if len(password)>=8:
    for i in password:
        if i.islower():
            check.add('l')
        elif i.isupper():
            check.add('u')
        elif i.isdigit():
            check.add('n')
        else:
            check.add('s')

    if len(check) == 4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")










        
        
