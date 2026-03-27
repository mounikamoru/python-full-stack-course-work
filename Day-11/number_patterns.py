'''for i in range(1,6):
    for j in range(1,6):    
        print(i,end="")
    print()

#11111
#22222
#33333
#44444
#55555

print("#------------------------------------------")
for i in range(1,6):
   for j in range(1,6):
       print(j,end="")
   print()
#12345
#12345
#12345
#12345
#12345

print("#------------------------------------------")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end="")
    print()
#55555
#44444
#33333
#22222
#11111

#---------------------------------------------------------
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end="")
    print()

#54321
#54321
#54321
#54321
#54321
print("#------------------------------------------")
#1 2 3 4 5
#6 7 8 9 10
#11 12 13 14 15
#16 17 18 19 20
#21 22 23 24 25

n =5 #size of the matrix
k= 1 #start value
for i in range(1,n+1): # 5 times controls the loop # each loop one row
    for j in range(1,n+1):
        print("{:2d}".format(k), end=" ")
        k +=1
    print()
print("#------------------------------------------")
#reversing 5/5 matriix
n=5
k=n*n
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k-=1
    print()
print("#------------------------------------------")
n=5
k=1

for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()
#1  3  5  7  9 

#11 13 15 17 19 

#21 23 25 27 29 

#31 33 35 37 39 

#41 43 45 47 49 
print("#------------------------------------------")
#reversing 
n=5
k=49

for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k-=2
    print()

print("#------------------------------------------")
#2  4  6  8 10 
#12 14 16 18 20 
#22 24 26 28 30 
#32 34 36 38 40 
#42 44 46 48 50 

n=5
k=2
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k+=2
    print()
print("#------------------------------------------")
# reversing
#output
#50 48 46 44 42 
#40 38 36 34 32 
#30 28 26 24 22

#20 18 16 14 12 
#10  8  6  4  2 

n=5
k=50
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end=" ")
        k-=2
    print()

print("#------------------------------------------")
n=5

for i in range(n):
    for j in range(n):
        num=i*n+j+1
        print("{:2d}".format(num),end=" ")
    print()

#1  2  3  4  5 
#6  7  8  9 10 
#11 12 13 14 15
#16 17 18 19 20 
#21 22 23 24 25 
print("#------------------------------------------")
n=5
for i in range(n):
    for j in range(n):
        num=n*n-(i*n+j)
        print("{:2d}".format(num),end=" ")
    print()
print("#------------------------------------------")    
#25 24 23 22 21 
#20 19 18 17 16 
#15 14 13 12 11 
#10  9  8  7  6 
#5  4  3  2  1

for i in range(1,6):
     for j in range(1,i+1):
         print((j*2) , end=" ")
     print()

#2 
#2 4 
#2 4 6 
#2 4 6 8 
#2 4 6 8 10
print("#------------------------------------------")
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

#5 
#5 4 
#5 4 3 
#5 4 3 2 
#5 4 3 2 1 


#----------------------------------------------------------------
#*****************************************************************
#pattern 1
#* * * * *   1 1 1 1 1
#* * * * *   1 1 1 1 1  
#* * * * *   1 1 1 1 1
#* * * * * 
#* * * * * 


for i in range(1,6):                  
    for j in range(1,6):
        print("*" , end=" ")
    print()
print("#------------------------------------------")
for i in range(1, 4):
    for j in range(1,4):
        print("1",end=" ")
    print()
print("#------------------------------------------")
#1 1 1 1 1     1 2 3 4 5    i  55555   j  54321
#2 2 2 2 2     1 2 3 4 5       44444      54321
#3 3 3 3 3     1 2 3 4 5       33333      54321
#4 4 4 4 4     1 2 3 4 5       22222      54321
#5 5 5 5 5     1 2 3 4 5       11111      54321

for i in range(1,6):
    for j in range(1,6):
        print( i , end =" ")
    print()
print("#------------------------------------------")
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()
print("#------------------------------------------")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end = " ")
    print()
print("#------------------------------------------")    
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end = " ")
    print()
print("#------------------------------------------")
n=5
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:2d}".format(k),end="" )
        k+=1
    print()
    
print("#------------------------------------------")
n=5
k=1
for i in range(1,n+1):
   for j in range(1,n+-1):
       print("{:2d}".format(k),end=" ")
       k+=2
   print()
print("#------------------------------------------")
for i in range(1,6):
    for j in range(1,4):
        print("{}{}".format(i,j),end="")
    print()
print("#------------------------------------------")    
for i in range(1,6):
    for j in range(1,4):
        print("{}{}".format(j,i),end="")
    print()

'''
print("#------------------------------------------")
print("#------------------------------------------")
#patterns2 0 and 1 ---even  and odd
#01010  10101
#01010  10101
#01010  10101
#01010  10101
#01010  10101

n=5
for i in range(1,6):
    for j in range(1,6):
        print((i+j+1)%2,end="")
    print()
print("#------------------------------------------")
n=5
for i in range(1,6):
    for j in range(1,6):
        print((i+j)%2,end="")
    print()


# ================================

n = int(input("Enter size: "))

# -------------------------------
# 1. Solid Square
# -------------------------------
print("\n1. Solid Square")
for i in range(n):
    print("* " * n)


# -------------------------------
# 2. Number Column Pattern
# -------------------------------
print("\n2. Column Numbers")
for i in range(n):
    for j in range(n):
        print(j, end=" ")
    print()


# -------------------------------
# 3. Row Number Pattern
# -------------------------------
print("\n3. Row Numbers")
for i in range(n):
    for j in range(n):
        print(i, end=" ")
    print()


# -------------------------------
# 4. 0-1 Pattern
# -------------------------------
print("\n4. 0-1 Pattern")
for i in range(n):
    for j in range(n):
        print((i + j) % 2, end=" ")
    print()


# -------------------------------
# 5. Right Triangle
# -------------------------------
print("\n5. Right Triangle")
for i in range(n):
    print("* " * (i + 1))


# -------------------------------
# 6. Reverse Triangle
# -------------------------------
print("\n6. Reverse Triangle")
for i in range(n):
    print("* " * (n - i))


# -------------------------------
# 7. Right Aligned Triangle
# -------------------------------
print("\n7. Right Aligned Triangle")
for i in range(n):
    print("  " * (n - i - 1) + "* " * (i + 1))


# -------------------------------
# 8. Reverse Right Aligned
# -------------------------------
print("\n8. Reverse Right Aligned")
for i in range(n):
    print("  " * i + "* " * (n - i))


# -------------------------------
# 9. Border Square
# -------------------------------
print("\n9. Border Square")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# -------------------------------
# 10. Middle Line Pattern
# -------------------------------
print("\n10. Border + Middle Row")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == n//2 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# -------------------------------
# 11. L-Shape Pattern
# -------------------------------
print("\n11. L Shape")
for i in range(n):
    for j in range(n):
        if i == n-1 or j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# -------------------------------
# 12. Pyramid
# -------------------------------
print("\n12. Pyramid")
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))


# -------------------------------
# 13. Inverted Pyramid
# -------------------------------
print("\n13. Inverted Pyramid")
for i in range(n):
    print(" " * i + "* " * (n - i))


# -------------------------------
# 14. Diamond Pattern
# -------------------------------
print("\n14. Diamond")

# upper
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))

# lower
for i in range(n - 1):
    print(" " * (i + 1) + "* " * (n - i - 1))



        

