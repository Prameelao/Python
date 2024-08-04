###Print First 10 Natural numbers
##for num in range(1,11):
##    print(num)


###Print all evn numbers within range
##for num in range(1,10):
##    if num%2==0:
##        print(num)
##        


##sum=0
##for num in range(11):
##    sum=sum+num
##print(sum)
##    


###To print sum of ODD numbers in range
##n=10
##sum=0
##for val in range(n+1):
##    if val%2!=0:
##        sum=sum+val
##print(sum)


###Print Multiplication table
##num=12
##n=10
##for mul in range(n+1):
##    print(num,"x",mul,'=',num*mul)


###To display numbers from list using for loop
##a=[1,2,"abc",(3,4),{6,7}]
##for list in a:
##    print(list)

###count total number of digits in a number
##num="123445"
##count=0
##for i in num:
##    count=count+1
##print(count)

##
##for num in range(0,41,5):
##    if num==15:
##      break
##    else:
##      print("num")
##
##


##num=10
##count=0
##for i in range(2,num//2):
##    if num%i==0:
##        count=count+1
##        print(count,'=',count,'+',1)
##if count==0:
##    print('prime')
##else:
##    print('not prime')
        

##num=7
##for i in range(2,num-1):
##    if num%i==0:
##        print('not a prime')
##        break
##else:
##    print('prime')



##num=7
##for i in range(2,int(num**(0.5))+1):
##    if num%i==0:
##        print('not a prime')
##        break
##else:
##    print('prime')



#TO CHECK GIVEN NUMBER IS AMSTRONG NUMBER OR NOT
##num=153
##copy=num
##power=len(str(num))
##sum=0
##while num!=0:
##    rem=num%10
##    rem=rem**power
##    sum=sum+rem
##    num=num//10
##if sum==copy:
##    print("amstrong")
##else:
##    print("not amstrong")
##


###TO CHECK NUBER IS A DISARM NUMBER OR NOT
##num=1123
##copy=num
##sum=0
##power=len(str(num))
##while num!=0:
##    rem=num%10
##    rem=rem**power
##    sum=sum+rem
##    num=num//10
##    power=power-1
##if copy==sum:
##    print("disarm")
##else:
##    print("not disarm")
##    
##


num=123
power=10**len(str(num))
sum=0
while num!=0:
    rem=num%10
    res=rem*power
    sum=sum-res
    num=num//10
    power=power//10
print(res)
    




























































