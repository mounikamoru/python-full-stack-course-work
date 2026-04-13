
#method -1

import logic

print(logic.add(5,4))
print(logic.sub(2,3))
print(logic.mul(1,4))
print(logic.div(5,3))
print(logic.mod(3,2))

#method -2

import logic as l

print(l.add(5,4))
print(l.sub(2,3))
print(l.mul(1,4))
print(l.div(5,3))
print(l.mod(3,2))

#method -3

from logic import add,sub,mul,div,mod

print(add(5,4))
print(sub(2,3))
print(mul(1,4))
print(div(5,3))
print(mod(3,2))


#method -4

from logic import *

print(add(5,4))
print(sub(2,3))
print(mul(1,4))
print(div(5,3))
print(mod(3,2))

'''
#method-1

import logic 
print(logic.likes)
print(logic.comments)

print(logic.addlike())
print(logic.addlike())
print(logic.addlike())

print(logic.addcomments("Good"))


#method-2

import logic as lg#alias name
print(lg.likes)
print(lg.comments)

print(lg.addlike())
print(lg.addlike())
print(lg.addlike())

print(lg.addcomments("Good"))


#method-3

from logic import likes,comments,addlike,addcomments
print(likes)
print(comments)

print(addlike())
print(addlike())
print(addlike())

print(
    addcomments("Good"))

#method-4
from logic import * #gives all func and variables
print(likes)
print(comments)

print(addlike())
print(addlike())
print(addlike())

print(
    addcomments("Good"))
'''
