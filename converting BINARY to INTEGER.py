num=1010
res=0
pow=0
while num!=0:
    rem=num%10
    res=res+rem*(2**pow)
    num//=10
    pow=pow+1
print(res)
