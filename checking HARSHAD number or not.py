#checking HARSHAD number or not
#harshad number means if the number  is divisible by sum of the digits of the number
num=50
copy=num
res=0
while num!=0:
    rem=num%10
    res=res+rem
    num//=10
if copy%res==0:
    print("Harshad Number")
else:
    print("Not Harshad nuber")
