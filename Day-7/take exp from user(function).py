def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def rem(a,b):
    return a+b


exp = input("enter your expression: ")

if '+' in exp:
    a,b = exp.split('+')
    print(add(int(a),int(b)))

elif '-' in exp:
    a,b = exp.split('-')
    print(sub(int(a), int(b)))

elif '*' in exp:
    a,b = exp.split('*')
    print(mul(int(a), int(b)))

elif '/' in exp:
    a,b = exp.split('/')
    print(div(int(a), int(b)))

elif '%' in exp:
    a,b = exp.split('%')
    print(rem(int(a), int(b)))


