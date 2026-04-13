#LAMBDA :
#A lambda function is a function without a name. It can take any number of arguments but only has one expression

#using def function and lambda function:
#using def
def wish(name):
    return f'hello {name}, welcome to python'
print(wish('mouni'))

#using lambda
wish = lambda name: f'hello {name}, welcome to python'
print(wish('mouni'))

#avg of three numbers
def addf(a,b,c):
    return (a+b+c)/3
print(addf(1,2,3))


add = lambda a,b,c: (a+b+c)/3
print(add(3,4,5))

#to a number is even or odd
def is_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(is_even(5))


is_evenl = lambda n: "even" if n%2==0 else "odd"
print(is_evenl(8))

#printing greater number
num = lambda a,b: "greater" if a>b else "lesser"
print(num(6,4))

#char in vowels
char = lambda a : "vol" if a in vol else "con"
vol = 'aeiouAEIOU'
print(char('a'))

#map- to update the entire list

def fun(l):
    for i in range(len(l)):
        l[i] = l[i].title()
    return l


l = ['mouni','sree','nani','anu']
res = list(map(lambda i:i.title(),l))
print(fun(l))
print(res)

#filter- to print based on a condition

def fun(l):
    res = []
    for i in range(len(l)):
        if l[i]%20 == 0:
            res.append(l[i])
    return res

l = [10,20,30,40]
res = list(filter(lambda i:i%20==0,l))

print(fun(l))
print(res)
   
l = [10,20,30,40,50,60,70]
res = list(filter(lambda i:i>=60,l))

print(res)

l = {'laptop':True, 'mouse':False,'iphone':True}
res = list(filter(lambda i:l[i],l))
print(res)


l = [1,0,2,3,0,1,3,4,5,5,6,2,3,5,6,7,8,2]
res = list(map(lambda i:i%2==0,l))
print(res)

#reduce-to return a single final value

from functools import reduce
l = [1,2,3,1,2,3,6,4,3,9]
res = reduce(lambda a,b:a*b,l)
print(res)

from functools import reduce
l = ['python','sql','java','html']
res = reduce(lambda a,b:a+' '+b,l)
print(res)

#print max num
numbers = [10, 5, 30, 25]
max_num = max(numbers, key=lambda x: x)
print(max_num)

#using lambda in dictionary
d = {'apple':30,'orange':25,'pineapple':60,'mango':50,'banana':40}
print(d)
print(sorted(d))
print(d.items())
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))
