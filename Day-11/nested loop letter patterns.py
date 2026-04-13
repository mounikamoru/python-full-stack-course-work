


#1.A

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-1 or i == n // 2:
            print("*",end = ' ')
        else:
            print(" ",end = " ")
    print()
'''
* * * * * 
*       * 
* * * * * 
*       * 
*       * 
'''
#2.B
n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == n // 2 or j == 0 or j == n-1:
            print("*",end = ' ')
        else:
            print(" ",end = " ")
    print()
'''
* * * * * 
*       * 
* * * * * 
*       * 
* * * * *
'''

#3.C
n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0  or j == 0 or i == n-1:
            print("*",end = ' ')
        else:
            print(" ",end = " ")
    print()
'''
* * * * * 
*         
*         
*         
* * * * *
'''

#4.D
n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0  or j == 0 or i == n-1 or j == n-1:
            print("*",end = ' ')
        else:
            print(" ",end = " ")
    print()
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * *
'''

#5.E
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == n // 2 or j == 0:
            print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*         
* * * * * 
*         
* * * * *
'''
#6.F

n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n // 2 or j == 0:
            print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*         
* * * * * 
*         
*
'''

#7.G
n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0  or j == 0 or i == n-1 or (i == n//2 and j >= n//2) or (j == n-1 and i >= n//2):
            print("*",end = ' ')
        else:
            print(" ",end = " ")
    print()
'''
* * * * * 
*         
*   * * * 
*       * 
* * * * * 
'''

#8.H
n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == n // 2:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
*       * 
* * * * * 
*       * 
*       *
'''

#9.I

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n // 2:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
    *     
    *     
    *     
* * * * *
'''

#10.J

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2 or (i == n-1 and j <= n //2) or (j == 0 and i >= n // 2):
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
    *     
*   *     
*   *     
* * *     
'''

#11.K

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i + j == n//2 or i - j == n//2:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*   *     
* *       
*         
* *       
*   *
'''

#12.L

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*         
*         
*         
*         
* * * * * 
'''

#13.M

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i <= n//2) or (i + j == n-1 and i <= n//2):
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
* *   * * 
*   *   * 
*       * 
*       *
'''

#14.N

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == j :
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
* *     * 
*   *   * 
*     * * 
*       * 
'''

#15. O

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n-1 :
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * *
'''

#16.P

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or (j == n-1 and i <= n //2) or i == n // 2:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*       * 
* * * * * 
*         
*         
'''

#17.Q

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == 0 or i == n-1 or (i == j and i >= n //2) :
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*       * 
*   *   * 
*     * * 
* * * * * 
'''

#18.R

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j ==0 or i == 0 or i == n // 2 or (j == n-1 and i <= n // 2) or (i == j and i >= n // 2) :
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*       * 
* * * * * 
*     *   
*       * 
'''

#19.S

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or (j == 0 and i <= n // 2) or i == n // 2 or (j == n-1 and i >= n // 2) or i == n-1 :
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
*         
* * * * * 
        * 
* * * * * 
'''

#20.T

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == n // 2:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
    *     
    *     
    *     
    *    
'''

#21.U

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1 or j == n-1:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
*       * 
*       * 
*       * 
* * * * *
'''

#22.V

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if (i == j and i <= n // 2) or (i+j == n-1 and i <= n // 2):
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*           * 
  *       *   
    *   *     
      *
'''

#23.W

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i+j == n-1 and i >= n // 2) or ( i == j and i >= n // 2) :
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
*       * 
*   *   * 
* *   * * 
*       *
''' 
#24. X

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i+j == n-1 or i == j:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
  *   *   
    *     
  *   *   
*       *
'''

#25.Y

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i+j == n-1 or (i == j and i <= n // 2):
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
  *   *   
    *     
  *       
*
'''

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if (i+j == n-1 and i <= n // 2) or (i == j and i <= n // 2) or (j == n // 2 and i >= n // 2):
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
*       * 
  *   *   
    *     
    *     
    *     
'''
#26.Z

n = int(input("enter the size: "))
for i in range(n):
    for j in range(n):
        if i+j == n-1 or i == 0 or i == n-1:
             print("*", end = ' ')
        else:
            print(" ",end = ' ')
    print()
'''
* * * * * 
      *   
    *     
  *       
* * * * * 
'''




'''
#1
n = int(input("enter the size:"))
for i in range(n):
    print("*")
*
*
*
*

#2.
n = int(input("enter the size:"))
for i in range(n):
    print("*",end = ' ')
* * * *


#3.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()
* * * * 
* * * * 
* * * * 
* * * * 


#4.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(i+1):
        print("*",end = " ")
    print()
* 
* * 
* * * 
* * * * 


#5.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n-i):
        print("*", end = ' ')
    print()
* * * * 
* * * 
* * 
*


#6.
n = int(input("enter the size:"))
for i in range(n):
    for spa in range(n-i-1):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=" ")
    print()
      * 
    * * 
  * * * 
* * * *



#7.
n = int(input("enter the size:"))
for i in range(n):
    for space in range(i):
        print(" ",end = ' ')
    for j in range(n-i):
        print("*",end= ' ')
    print()
* * * * 
  * * * 
    * * 
      * 

#8.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        print(i, end = " ")
    print()
0 0 0 0 
1 1 1 1 
2 2 2 2 
3 3 3 3 


#9.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        print(j,end= " ")
    print()
0 1 2 3 
0 1 2 3 
0 1 2 3 
0 1 2 3 

#10.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
* * * * 
*     * 
*     * 
* * * *   


#11.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i == n // 2 or j == 0 or j == n-1 or j == n // 2:
            print("*",end = ' ')
        else:
            print(" ",end = ' ')
    print()


#12.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == n-i-1:#i+j==n-1
            print("*",end = ' ')
        else:
            print(" ",end = ' ')
    print()
* * * * * 
      *   
    *     
  *       
* * * * *

#13.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i == j or j == n-i-1:#i+j=n-1
            print("*",end = ' ')
        else:
            print(" ",end = ' ')
    print()
*       * 
  *   *   
    *     
  *   *   
*       * 


#14.
n = int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
'''
