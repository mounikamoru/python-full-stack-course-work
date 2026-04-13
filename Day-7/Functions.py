#---------------------------FUNCTIONS------------------------------
# syntax
def function_name(arg):
    #stmts
    return
function_name(para)

#function example:
def wish(name):
    print(f' Hello, {name} - welcome to codegnan')

wish('mounika')
wish('himaja')

#four types of argumenyts
  #**1.positional arguments**

def details(name,DOB,age):
    print("name: ",name)
    print("DOB: ",DOB)
    print("age: ",age)
details('mouni','010104','22')
details('010104','anju','22')
details('22','010104','anju')

  #**2.keyword arguments**

details(name='mouni',DOB='010104',age='22')
details(DOB='010104',name='mouni',age='22')
details(age='22',DOB='010104',name='mouni')

  #**3.default argument

def details(name,DOB,age,phone_no= '+91'):
    print("name: ",name)
    print("DOB: ",DOB)
    print("age: ",age)
    print("phone_no:",phone_no)

details('mouni','010104','22')
details('nani','010105','21','876908')

  #**4.variable length argument

def display(*names):
    print("names:", names)
display('mouni','nani','hima')
display('mouni')

def display(**names):
    print("names:", names)
display(n1='mouni',n2='nani',n3='hima')
display(n1='mouni')
