#system module

import sys

print(sys.argv) #argv - to pass arguments instead of variables
                #gives arguments in the form of list
print(sys.path) #path - where the file is located
                #to retrive all the python libraries
print(sys.version) #version - python version and when it is installed
print(sys.exit) #exit - to terminate the program

#exit(important example
print("start")
print(sys.exit()) or sys.exit()
print("end")


#platform module

import platform
print(platform.system()) #system - return OS name (windows, Linux)
print(platform.release()) #release - OS release version
print(platform.processor()) #processor - return processor type

#math module

import math

print(math.pi) # for angles
print(math.e)

print(math.sqrt(4)) #gives sqrt in float value
print(math.pow(3,4))

print(math.ceil(12.000001))
print(math.floor(12.000001))

print(round(12.999))
print(abs(-12))
print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(12,8))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))


# collections module
counter,defaultdict,deque
counter - counts the repeating elements gives the results in dict format like value:repeated times
freqency of a particular item

import collections
s = 'python programming'
l = [2,3,4,5,5,1,1,2,1,2,3,4,5]
r = 'this is that that is this'.split()

res = collections.Counter(s)
res1 = collections.Counter(l)
res2= collections.Counter(r)
print(res)
print(res1)
print(res2)


res = collections.defaultdict(int)
for i in s:
    res[i] = res[i] + 1
print(res)


import collections
# deque used to pop from left and append at left
q=collections.deque([])
q.append(20)
q.append(30)
q.append(40)
q.append(50)
q.append(60)
q.append(70)
q.popleft()
q.popleft()
q.popleft()
q.append(10)
q.append(40)
q.appendleft(5)
print(q)


#if we want to append at left

q=collections.deque([])
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.appendleft(50)
q.appendleft(60)
q.appendleft(70)
q.pop()
q.pop()
q.pop()
q.appendleft(10)
q.appendleft(40)
q.appendleft(5)
print(q)

from itertools import combinations, permutations

s = 'abc'
print(list(combinations(s, 3)))
print(list(permutations(s, 3)))

