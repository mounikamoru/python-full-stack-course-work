name=input('enter the name:') #input for the string,
print(name)                            #default input type is string
age=int(input('enter your age:')) #input for the integer
print(age)
marks=float(input('enter your marks:')) #input for the float
print(marks)
names =input('enter your names:(space separated)').split() #input for the list
print(names)
names =input('enter your names:(comma separated)').split(',')
print(names)
numbers=list(map(int,input('enter your numbers:').split())) #input of integers for the list
print(numbers)
num1=list(map(float,input('enter your numbers:').split())) #input of float for the list
print(num1)
num2=list(input('enter your names:').split()) #input of strings for the list
print(num2)
num3=tuple(input('enter your names:').split()) #input of strings for the tuple
print(num3)
num4=tuple(map(int,input('enter your nums:').split())) #input of integers for the tuple
print(num4)
num5=tuple(map(float,input('enter your nums:').split())) #input of float for the tuple
print(num5)
num6=set(input('enter your nums:').split()) #input of string for the set
print(num6)
num7=set(map(int,input('enter your nums:').split())) #input of integers for the set
print(num7)
num8=set(map(float,input('enter your nums:').split())) #input of float for the set
print(num8)
d = eval(input('enter the input:')) #input for the dictionary
print(d)
# enter the input:{1:1,2:4,3:9}              
# {1: 1, 2: 4, 3: 9}
dict = eval(input('enter the input:'))
print(dict)
# enter the input:(1,2,3,4)            
#(1, 2, 3, 4)
