print('1.ARITHMETIC OPERATOR- used for basic mathematical calculations')

a,b = 6,5
print(a+b)  #addition operator
print(a-b)  #subtractio operator
print(a*b)  #multipication operator
print(a/b)  #division operator
print(a//b) #floor division
print(a%b)  #modulus operator
print(a**b) #exponent operator

print('2.COMPARISON OPERATOR- compare two values and return True or False')

x,y = 10,5
print(x == y)  #equal to
print(x != y)  #not equal to
print(x > y)   #Greater than
print(x < y)   #Less than
print(x >= 10) #Greater than or Equal to
print(y <= 5)  #Less than or Equal to

print('3.ASSIGNMENT OPERATOR- used to assign or update the value of a variable')

x = 10  #assign
x += 5  #add and assign(x = x + 5 → 15)
x -= 10 #subtract and assign(x = x - 10 → 5)
x *= 2  #multiply and assign(x = x * 2 → 10)
x /= 2  #division and assign(x = x/2 -> 5)
x //= 3 #floor divide and assign(x = x//3 -> 1)
x %= 1  #modulus and assign(x = x%1 -> 0)
x **= 5 #exponentiate and assign(x = x^5 -> 0)
print(x)

print('4.LOGICAL OPERATOR(USING LOGIC GATES)- used to combine multiple conditions')

x = 55
y = 66
print(x > 50 and y < 60) #True (Both conditions are True)
print(x > 58 or y < 68) #True (At least one condition is True)
print(not (x > 50))      #False (Reverses the True condition)

print('5.MEMBERSHIP OPERATORS- check if a value exists within a sequence')
# USING In and Not In

subjects = ["ds", "aiml", "sql", "html"]
print("aiml" in subjects)      #True
print("mysql" not in subjects) #True

print('6.IDENTITY OPERATORS- check whether two variables refer to the same object in memory')
# USING is and is not

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)     #True (Both refer to the same object)
print(a is c)     #False (Different objects with the same content)
print(a is not c) #True

print('7.BITWISE OPERATORS(WITH BINARY REPRESENTATION)- perform operations on the binary representation of numbers')

x = 5         #0101
y = 3         #0011
print(x & y)  #1 (Binary: 0001 → AND operation)
print(x | y)  #7 (Binary: 0111 → OR operation)
print(x ^ y)  #6 (Binary: 0110 → XOR operation)
print(~x)     #-6 (Binary: Inverts bits of 5)
print(x << 1) #10 (Binary: 1010 → Shifts left by 1)
print(x >> 1) #2 (Binary: 0010 → Shifts right by 1)
