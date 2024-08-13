num=1234
rev=0
ln=(len(str(num))-1)
power=(10**ln)
while num!=0:
    rem=num%10
    rev=rev+rem*power
    num//=10
    power//=10
print(rev)
