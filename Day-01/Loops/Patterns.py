##n=3
##for row in range(3):
##    for col in range(3):
##     print("*" ,end=' ')
##

##n=5
##for row in range(5):
##    for col in range(row+1):
##        print("*" ,end=" ")
####    print()

##n=5
##for row in range(5,0,-1):
##    for col in range(row):
##        print("*", end=" ")
##    print()

##
##n=5
##for row in range(5,0,-1):
##    for space in range(row-1):
##        print(" ", end=" ")
##    for star in range(n-(row-1)):
##        print("*", end= " ")
##    print()



##n=5
##for row in range(1,6):
##    for space in range(n-row):
##        print(" ", end=" ")
##    for star in range(row):
##        print("*", end= " ")
##    print()






##n=5
##for row in range(5):
##    for space in range(row):
##        print(' ',end=' ')
##    for star in range(n-row):
##        print("*",end=' ')
##    print()
##       
    

##n=4
##for row in range(1,5):
##    for sp in range(n-row):
##        print(' ',end=' ' )
##    for st in range(row*2-1):
##        print('*' ,end=' ' )
##    for sp in range(n-row):
##        print(' ',end=' ' )
##    print()
##
##


##n=4
##for i in range(4,0,-1):
##    for sp in range(n-i):
##        print(' ',end=' ')
##    for st in range(i*2-1):
##        print('*',end=' ')
##print()
##


##n=5
##for i in range(5):
##    for sp in range(n-(i+1)):
##        print(end=' ')
##    for st in range(i+1):
##        print('*',end=' ')
##    print()
##

##* * * * * * * 
## * * * * * * 
##  * * * * * 
##   * * * * 
##    * * * 
##     * * 
##      * 

##n=7
##for i in range(7):
##    for sp in range(i):
##        print(end=' ')
##    for st in range(n-i):
##        print('*',end=' ')
##    print()
##

##        1 
##      1 2 
##    1 2 3 
##  1 2 3 4 
##1 2 3 4 5

##n=5
##for i in range(1,n+1):
##    for sp in range(0,n-i):
##        print(' ',end=' ')
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()
##



##1 
##2 1 
##3 2 1 
##4 3 2 1 
##5 4 3 2 1 

##n=5
##for i in range(1,n+1):
##    for j in range(i,0,-1):
##        print(j,end=' ')
##    print()


##5 4 3 2 1 
##4 3 2 1 
##3 2 1 
##2 1 
##1 


##n=5
##for i in range(n,0,-1):
##    for j in range(i,0,-1):
##        print(j,end=' ')
##    print()


##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1

n=10
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j,end=' ')
    print()



















































































































































