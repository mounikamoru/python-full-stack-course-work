'''def display(n):
    if n>10:
        return
    print("Before:",n)
    display(n+1)
    print("After:",n)

display(1)

display("Python Programming")


def display(s,i):
    if i==len(s):
        return
    display(s,i+1)
    print(s[i])
display("Python Programming",0)


def display(s,i):
    if i==len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display("Python Programming",0)


def display(s,i):
    if i<=0:
        return
    display(s,i-1)
    print(s*i)
display("abc",5)


def display(s,i):
    if i<=0:
        return
    display(s,i-1)
    print(s*i)
display("abc",5)

def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display("abcefghijkl",0,5)

def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display([1,2,3,4,5,6,7,8],0,0))
      


def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display(['python','java','html','css','javascript','flask'],0,''))

'''
#pass by value and pass by reference
#int,float,list,tuple,set,dict,str

def display(n):
    n+=(8,9)
    print("Inside:",n)


n=(1,2,3,4)
display(n)
print("outside:",n)
