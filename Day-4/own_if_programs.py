'''#even or odd
num=int(input("enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")

#total and average
m1=int(input("enter the marks 1:"))
m2=int(input("enter the marks 2:"))
m3=int(input("enter the marks 3:"))
total=m1+m2+m3
average=total/3
print("taotal=",total)
print("average=",average)


#largest of three numbers
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>=b and a>=c:
    print("largest number is",a)
elif b>=a and b>=c:
    print("largest number is",b)
else:
    print("largest number is",c)


#largest of two numbers
a=int(input("enter the firsst number:"))
b=int(input("enter the second number:"))
if a>=b:
    print("largest number is",a)
elif b>=a:
    print("largest number is",b)
'''
#print 1 to 10 in same line
for i in range(1,11):
  print(i,end="")

    
