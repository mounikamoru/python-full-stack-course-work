n = int(input("enter the size: "))   #* * * * 
for row in range(n):                 #* * * * 
    for col in range(n):             #* * * * 
        print('*', end= ' ')         #* * * * 
    print()


n = int(input("enter the size: "))   
for row in range(n):                  #0 0 0 0
    for col in range(n):              #1 1 1 1
        print(row, end= ' ')          #2 2 2 2
    print()                           #3 3 3 3


n = int(input("enter the size: "))
for row in range(n):                  #0 1 2 3
    for col in range(n):              #0 1 2 3
        print(col, end= ' ')          #0 1 2 3
    print()                           #0 1 2 3

n = int(input("enter the size: "))
for row in range(n):                  #0 1 0 1
    for col in range(n):              #1 0 1 0
        print((row+col)%2, end= ' ')  #0 1 0 1
    print()                           #1 0 1 0

n = int(input("enter the size: "))
for i in range(n):
    for j in range(i+1):            # *
        print("*",end = ' ')        # * *
    print()                         # * * *
      
n = int(input("enter the size: "))
for i in range(n):                  # * * *
    for j in range(n-i):            # * * 
        print("*",end =' ')         # *
    print()

n = int(input("enter the size: "))
for i in range(n):
    for space in range(n-i-1):       #       *
        print(" ",end= ' ')          #     * *
    for j in range(i+1):             #   * * *
        print("*",end =' ')          # * * * *
    print()

n = int(input("enter the size: "))
for i in range(n):        
    for space in range(i):          # * * * *
        print(" ",end= ' ')         #   * * *
    for j in range(n-i):            #     * *
        print("*",end =' ')         #       *
    print()

n = int(input("enter the size: "))
for row in range(n):
    for col in range(n):                                       # * * * * 
        if row == 0 or row == n-1 or col == 0 or col == n-1:   # *     *
            print('*',end = ' ')                               # *     *
        else:                                                  # * * * *
            print(' ',end = ' ')
    print()

n = int(input("enter the size: "))
for row in range(n):
    for col in range(n):                                                                   #  * * * * *
        if row == 0 or row == n-1 or col == 0 or col == n-1 or row==n//2 or col==n//2:     #  *   *   *
            print('*',end = ' ')                                                           #  * * * * *
        else:                                                                              #  *   *   *
            print(' ',end = ' ')                                                           #  * * * * * 
    print()

n = int(input("enter the size: "))
for row in range(n):
    for col in range(n):                               # * * * * * 
        if row == 0 or row==n-1 or  row+col==n-1:      #       *
            print('*',end = ' ')                       #     *
        else:                                          #   *
            print(' ',end = ' ')                       # * * * * * 
    print()

n = int(input("enter the size: "))
for row in range(n):
    for col in range(n):                               # *   *
        if row == col or  row+col==n-1:                #  * *
            print('*',end = ' ')                       #   *
        else:                                          #  * *
            print(' ',end = ' ')                       # *   *
    print()
            

