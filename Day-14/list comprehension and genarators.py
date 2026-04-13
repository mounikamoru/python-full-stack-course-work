#LIST COMPREHENSION

#multiple of 2
a = []
for i in range(1,100):
    if i % 2 == 0:
        a.append(i)
print(a)

l = [i for i in range(1,100) if i%2==0]
print(l)

#multiple of 3
l = [i for i in range(3,99,3)]
print(l)

l = []
for i in range(1,101):
    if i %3 == 0:
        l.append(i)
print(l)


#squares of numbers using list comprehension
l = [i*i for i in range(1,11)]
print(l)


#numbers greater than 5

l = [5,3,21,2,17,8,1,0]

s = 'python programming'
vol = 'aeiouAEIOU'
l = ['*' if i in vol else i for i in s]
print(l)


#printing even numbers and 0 in place of odd numbers
l = [7,2,3,4,1,7,8,9,3,5,0,8]
l = [i if i%2==0 else 0 for i in l]
print(l)

#set
l = [7,2,3,4,1,7,8,9,3,5,0,8]
l = {i if i%2==0 else 0 for i in l}
print(l)

'''
same for the set just change the braces and it will remove the duplicate elements
there is no list compre for tuple
we have generator for tuple
'''

#printing the tuple of elements using generator
l = [7,2,3,4,1,7,8,9,3,5,0,8]
l = tuple(i if i%2==0 else 0 for i in l)
print(l)

#dict
l = [7,2,3,4,1,7,8,9,3,5,0,8]
r = {i:l.count(i) for i in l}
print(r)

#genarator example
def reels():
    r = ['1..100','2...200','3...300','4..400','5..500']
    for i in r:
        yield i
scroll = reels()
print(next(scroll))
print(next(scroll))

'''
yeild is like pausing
return is like exit
'''

def display():
    yield "pfs-50"
    yield "pfs-29"
    yield "pfs-60"
leave = display()
for i in range(3):
    print(next(leave))
