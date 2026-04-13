
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

'''
likes = 0
comments = []

def addlike():
    global likes # to effect outside we can use this becoz int doesnot effect outside
    likes+=1
    return likes

def addcomments(com=None): #if user didn't passed any comment then the default is none
    comments.append(com) #here we don't need to write global comments becoz list effect the outside value
    return comments

print(addlike())
print(addcomments("Good"))
print(addcomments("Better"))
'''
