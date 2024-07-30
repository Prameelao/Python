##1 1 1 1 1 
##1 1 1 1 1 
##1 1 1 1 1 
##1 1 1 1 1 
##1 1 1 1 1 
##n=5
##for i in range(n):
##    for j in range(n):
##        print(1,end=' ')
##    print()


##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5 
##n=5
##for i in range(1,n+1):
##    for j in range(i):
##        print(i,end=' ')
##    print()

##5 5 5 5 5 
##4 4 4 4 
##3 3 3 
##2 2 
##1 
##
##n=5
##for i in range(n,0,-1):
##    for j in range(i):
##        print(i,end=' ')
##    print()

##5 
##4 4 
##3 3 3 
##2 2 2 2 
##1 1 1 1 1 
##
##n=5
##for i in range(n,0,-1):#5,4,3,2,1
##    for j in range(n-i+1):
##        print(i,end=' ')
##    print()

##        5 
##      4 4 
##    3 3 3 
##  2 2 2 2 
##1 1 1 1 1 
##n=5
##for i in range(n,0,-1): #5,4,3,2,1
##    for sp in range(i-1):
##        print(' ',end=' ')
##    for col in range(n-i+1):
##        print(i,end=' ')
##    print()
##

##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5 
##
##n=5
##for i in range(1,n+1):
##    for col in range(i):
##        print(i,end=' ')
##    print()

##1 1 1 1 1 
##2 2 2 2 
##3 3 3 
##4 4 
##5 
##
##n=5
##for i in range(1,n+1): #1,2,3,4,5
##    for j in range(n-i+1):
##        print(i,end=' ')
##    print()


##1 1 1 1 1 
##  2 2 2 2 
##    3 3 3 
##      4 4 
##        5 
##n=5
##for i in range(1,n+1): #1,2,3,4,5    0,1,2,3,4(sp)
##    for sp in range(i-1):
##        print(' ',end=' ')
##    for j in range(n-i+1):
##        print(i,end=' ')
##    print()

##        1 
##      2 2 
##    3 3 3 
##  4 4 4 4 
##5 5 5 5 5 
##n=5
##for i in range(1,n+1):
##    for sp in range(n-i):
##        print(' ',end=' ')
##    for col in range(i):
##        print(i,end=' ')
##    print()

##5 5 5 5 5 
##  4 4 4 4 
##    3 3 3 
##      2 2 
##        1 
##n=5
##for i in range(5,0,-1):
##    for sp in range(n-i):
##        print(' ',end=' ')
##    for j in range(i):
##        print(i,end=' ')
##    print()

##        1 
##      1 2 
##    1 2 3 
##  1 2 3 4 
##1 2 3 4 5 
##n=5
##for i in range(1,n+1):
##    for sp in range(n-i):
##        print(' ',end=' ')
##    for col in range(1,i+1):
##        print(col,end=' ')
##    print()
##
##

##1 
##3 3 
##5 5 5 
##7 7 7 7 
##9 9 9 9 9
##
##n=5
##odd=1
##for i in range(1,n+1):
##    for j in range(i):
##        print(odd,end=' ')
##    print()
##    odd+=2



































    









































































































































