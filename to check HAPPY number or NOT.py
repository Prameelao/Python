#to check given number is HAPPY number or NOT
num=12
while num>9:
    sum=0
    while num!=0:
       last=num%10
       sum=sum+last**2
       num//=10
    num=sum
if num==1 or num==7:
    print("HAPPY number")
else:
    print("not HAPPY number")
    
