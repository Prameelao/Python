#CONVERTING INTEGER TO BINARY
num=10
res=0
pos=1
while num!=0:
    rem=num%2
    res=res+rem*pos
    num//=2
    pos*=10
print(res)
    
