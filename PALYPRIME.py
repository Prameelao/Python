#to check POLYPRIME or NOT
#condition single 1,7 if it is double make single by doingsum of squares of digits
##num=11
##copy=num
##for den in range(2,num//2+1):
##     if num%den==0:
##         break
##     else:
##        print("not POLYPRIME")
##else:
##    rev=0
##    pos=10**(len(str(copy))-1)
##    while copy!=0:
##        rem=copy%10
##        rev=rev+rem*pos
##        copy//=10
##        pos//=10
##    if copy==rev:
##        print("POLY PRIME")
##    else:
##        print("NOT POLY PRIME")
##
##         
         
num=131
rev=0
copy=num
while num!=0:
     last=num%10
     rev=rev*10+last
     num//=10
if copy==rev:
    fc=0
    for den in range(2,copy//2+1):
       if copy%den==0:
           fc+=1
           if fc==2:
               print("palyprime")
           else:
               print('Not palyprime')
    else:
          print('Not palyprime')
else:
    print('Not palyprime')
          
        



































