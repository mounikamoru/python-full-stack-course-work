

#1.Write a list comprehension to create a list of odd numbers from 1 to 20.

l = [i for i in range(1,21,2)]
print(l)


#2.Create a list of multiples of 5 between 5 and 50 using list comprehension.

m = [i for i in range(5,51,5)]
print(m)


#3.Create a list containing the cube of numbers from 1 to 10.

c = [i**3 for i in range(1,11)]
print(c)


#4.From the list below, create a new list containing numbers less than 10.

l = [3,12,7,18,5,21,9]
n =[i for i in l if i < 10]
print(n)


#5.From the list:Create a new list where negative numbers become 0.

l = [4,-2,7,-5,9,-1]
z = [i if i > 0 else 0 for i in l]
print(z)

#6.From the string:Create a list containing only vowels.

s = "education"
v = 'aeiou'
vol = [i for i in s if i in v]
print(vol)

#7.From the list:Create a list where odd numbers become 0.

n = [1,2,3,4,5,6,7,8]
o = [i if i%2==0 else 0 for i in n]
print(o)

#8.Create a set containing squares of numbers from 1 to 10.

squ = {i**2 for i in range(1,11)}
print(squ)

#9.Create a tuple of even numbers from 2 to 20 using comprehension.

t = tuple(i for i in range(2,21,2))
print(t)

#10.Create a dictionary where:key → number,value → cube of the number
     #For numbers 1 to 5.

d = {i:i**3 for i in range(1,6)}
print(d)

#11.From the list:Create a dictionary showing frequency of each element.

n = [2,3,2,5,3,2,4]
d = {i:n.count(i) for i in n}
print(d)

#12.Write a generator that yields multiples of 4 up to 40.

def mul():
    n = 4
    for i in range(1,11):
        a = n*i
        yield a
times = mul()
for i in range(10):
    print(next(times))

#13.Create a generator that counts down from 10 to 1.

def down():
    for i in range(10,0,-1):
        yield i
count = down()
for i in range(10):
    print(next(count))

#14.From the list below, create a new list containing only numbers divisible by 3.

nums = [4, 9, 12, 7, 6, 15, 10, 3]
d = [i for i in nums if i %3 ==0]
print(d)

#15.From 1–20, create a list containing squares of only even numbers.

a = [i*i for i in range(2,21,2)]
print(a)

#16.From the list below, create a list of words with more than 4 letters.

words = ["sun","planet","sky","galaxy","star","universe"]
a = [i for i in words if len(i) > 4]
print(a)

#17.From the list below, create a list containing only the first letter of each word.

words = ["apple","banana","cherry","mango"]
l = [i[0] for i in words]
print(l)


#18.Convert all words in the list to uppercase.

words = ["python","java","c","go"]
u = [i.upper() for i in words]
print(u)

#19.From 1–50, create a list of numbers divisible by 3 OR 5.

a = [i for i in range(1,51) if i % 3 == 0 or i % 5 == 0]
print(a)

#20.Flatten the nested list.

l = [[1,2],[3,4],[5,6]] #[1,2,3,4,5,6]
f = [i for sublist in l for i in sublist]
print(f)

#21.Create a list of characters from the string except vowels.

s = "education"
c = [i for i in s if i not in 'aeiou' ]
print(c)

#22.Create a list for the multiplication table of 7 from 7 × 1 to 7 × 10.
n = 7
seven=[f'{n}*{i} = {n*i}'for i in range(1,11)]
print(seven)


#23.Create a list containing the length of each word.

words = ["python","is","very","powerful"]
l = {i:len(i) for i in words}
print(l)

l = [len(i) for i in words]
print(l)


#24.Create all pairs (i, j) where i and j range from 1–3.
    #Expected output example:
    #[(1,1),(1,2),(1,3),(2,1)...]

t = [(i,j) for i in range(1,4) for j in range(1,4)]
print(t)


#25.Extract only even numbers.

l = [[2,3,4],[5,6,7],[8,9]]

e = [i for sublist in l for i in sublist if i % 2 == 0]
print(e)

#26.Create a list containing reversed words.

words = ["python","code","learn"]
r = [i[::-1] for i in words]
print(r)

#27.Create a list of characters except spaces.

s = "python list comprehension"
char = [i for i in s if i != " "]
print(char)

#28.Create a list of tuples (number, square) from 1–10.

t = tuple((i,i**2) for i in range(1,11))
print(t)

#29.Create a list containing ASCII values of characters in:

s = 'abcde'
a = [ord(i) for i in s]
print(a)

#30.Extract only palindrome words.

words = ["level","python","radar","code","madam"]
palin=[i for i in words if i == i[::-1]]
print(palin)


#31.From 1–20, create a list of square of odd numbers only.

squ_odd =[i**2 for i in range(1,21,2)]
print(squ_odd)

#32.From the list:Create a list where:even → square,odd → cube


nums = [2,7,4,9,6]
l = [i**2 if i%2==0 else i**3 for i in nums]
print(l)

#33.Create a 3×3 matrix using list comprehension.
m = [[0 for i in range(3)] for j in range(3)]
print(m)


#1.
a = [i for i in range(1,11) if i % 2==0]
print(a)

#or

a = [i for i in range(2,11,2)]
print(a)

#2.
b = [i for i in range(3,16,3)]
print(b)

#3.
c = [i**2 for i in range(1,11)]
print(c)

#4.
l = [1,3,4,7,2,9,6,8]
d = [i for i in l if i >5]
print(d)

#5.
l = [5,3,21,2,17,8,1,0]
a = [i if i > 5 else 0 for i in l]

#6.
s = 'anjusree'
vol = 'aeiouAEIOU'
l = [i if i in vol else 0 for i in s]
print(l)

#7.
n = [6,8,5,4,7,6,9,0,3,2,5,1,1]
l = [0 if i%2 == 0 else i for i in n]
print(l)

#8.
n = [6,8,5,4,7,6,9,0,3,2,5,1,1]
l = {0 if i%2 == 0 else i for i in n}
print(l)

#9.
n = [6,8,5,4,7,6,9,0,3,2,5,1,1]
l = tuple(0 if i%2 == 0 else i for i in n)
print(l)

#10.
n = {1:1,2:4,3:9,4:16,5:25}
l = [i if i%2==0 else 0 for i in n]
print(l)

#11.
n = [6,8,5,4,7,6,9,0,3,2,5,1,1]
r = {i:n.count(i) for i in n}
print(r)

#12.
def reels():
    r = ['1..100','2..200','3..300']
    for i in r:
        yield i
scroll = reels()
print(next(scroll))
print(next(scroll))

#13.

def alarm():
    t = ['6:00','7:00','8:00','9:00']
    for i in t:
        yield i
ring = alarm()
for i in range(2):
    print(next(ring))
    

