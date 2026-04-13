#recursion-func. calling itself is called recursion/ function called inside the function
#two keywords: def and return
#LIFO
'''
syntax:
def fun():
    if base_con:
        return
    fun()
'''

#printing numbers from 1 to 10
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)


#printing numbers from 10 to 1
def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)


#printing numbers from 1 to 10 and 10 to 1
def display(n):
    if n>10:
        return
    print("before",n)
    display(n+1)
    print("after",n)
display(1)


#printing the each character of the string
def display(s,i):
    if i == len(s):
        return
    print(s[i])
    display(s,i+1)
display('python programming',0)


#printing the each character of the string in reverse order
def display(s,i):
    if i == len(s):
        return
    display(s,i+1)
    print(s[i])
display('python programming',0)

#
def display(s,i):
    if i == len(s):
        return
    print(s[:i+1])
    display(s,i+1)
display('python programming',0)
'''
p
py
pyt
pyth
pytho
python
python 
python p
python pr
'''

#
def display(s,i):
    if i<=0:
        return
    print(s*i)
    display(s,i-1)
display('abc',5)
'''
abcabcabcabcabc
abcabcabcabc
abcabcabc
abcabc
abc
'''

#
def display(s,i,n):
    if i == len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)
display('abcdefg',0,3)
'''
abc
bcd
cde
def
'''

#sum of list
def display(l,i,sum):
    if i == len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display([1,2,3,4,5,6,7,8],0,0))
#36


#printing the elements in a single string(method-1)
def display(l,i,sum):
    if i == len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display(['java','python','sql'],0,' '))

#method-2
def display(s,i):
    if i == len(s):
        return
    print(s[i],end = '')
    display(s,i+1)
display(['java','python','sql'],0)



'''pass by value - immutable items 
pass by reference - muttable whatever done inside the fuc will effect the outerfunc'''



#int,float,str,list,tuple,set,dict

#
def display(n):
    n = 8 
    print("inside:",n)

n = 10
display(n)
print("Outside:",n)

#    
def display(n):
    n = 10.4 
    print("inside:",n)

n = 10.9
display(n)
print("Outside:",n)

#
def display(n):
    n = 'anju' + n
    print("inside:",n)

n = 'sree'
display(n)
print("Outside:",n)

#
def display(n):
    n.extend([1,2])
    print("inside:",n)

n = [3,4]
display(n)
print("Outside:",n)

#
def display(n):
    n+=(8,9)
    print("inside:",n)

n = (3,4)
display(n)
print("Outside:",n)

#
def display(n):
    n.update({1,2})
    print("inside:",n)

n = {3,4}
display(n)
print("Outside:",n)

#
def display(n):
    n[5] =6
    print("inside:",n)

n = {3:4}
display(n)
print("Outside:",n)
