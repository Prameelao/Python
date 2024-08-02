num=145
copy=num
sum=0
while num!=0:
    rem=num%10
    fact=1
    for val in range(1,rem+1):
        fact=fact*val
    sum=sum+fact
    num//=10
if copy==sum:
    print("Strong Number")
else:
    print("Not Strong Number")
        
