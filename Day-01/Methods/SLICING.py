#SLICING
#on STRING
s='pramee is a good girl'
print(s[0:5:1])
print(s[::1])
print(s[1::])
print(s[::])                 #for +ve slicing STARTING INDEX<ENDING INDEX
print(s[6:10:2])
print(s[5:2:])
print(s[-5:10:-2])
print(s[::-1])
print(s[-2:10:-2])
print(s[-8:-2:-1])
print(s[-8:-2:1])

#on LIST
a=[8,5.5,3+2j,True,'str',[1,2],(3,4),{6,7},{'a':5,'b':8}]
print(a)
print(a[::1])
print(a[::-1])
print(a[2:20:2])
print(a[-2:-20:-2])
print(a[2:-5:3])
print(a[-2:-5:2])

#on TUPLE
a=(8,5.5,3+2j,True,'str',[1,2],(3,4),{6,7},{'a':5,'b':8})
print(a)
print(a[::1])
print(a[::-1])
print(a[2:20:2])
print(a[-2:-20:-2])
print(a[2:-5:3])
print(a[-2:-5:2])



#SLICE()
a=[8,5.5,3+2j,True,'str',[1,2],(3,4),{6,7},{'a':5,'b':8}]
n=slice[::]
print(a[n])


