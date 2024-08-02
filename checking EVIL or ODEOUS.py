#checking EVIL number or ODEOUS
num=11
count=0
while num!=0:
    rem=num%2
    if rem==1:
        count=count+1
    num//=2
if count%2==0:
    print("evil")
else:
    print("Odeous")
