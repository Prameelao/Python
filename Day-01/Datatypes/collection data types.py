#COLLECTION DATA TYPES
#STRING
a='prameela oruganti'
#orderd,duplicates allowed,indexing allowed
print(a)
print(a[9])
print(a[-10])
print(len(a))
print("type of a is :",type(a))
b='prameela      oruganti'
print(b)
print(b[9])
print(b[-10])
#string is IMMUTABLE
#LIST
var=[30,40,50,'str',5.5,True,'True',5+8j]
print("type of var is : " ,type(var))
print(var)
print(len(var))
print(var[3])
n=[(5,7),[8,9],{6,8},{a:5},[8,9]]
n[1][0]=7
print(n)
n="str{'t':7}"
print(n)
#TUPLE
apple=(5,7.8,'true',True,6+8j)
print(apple)
pramee=([5,6,7],(94,8,9),{5,7},{'p':6},{5,7})
print(pramee)
print('length of pramee is :',len(pramee))
print(pramee[0][1])
#SET
pra={4,6.8,'TRue',True,7+5j}
print(pra)
ammu={'stru',(3,5,6),'stru'}
print(ammu)
print(type(ammu))
#DICTIONARY
a={(6,7):5,'p':34,'5':5,'q':5,(6,7):10,5:5}
print(a)
print(type(a))
print(a[(6,7)])


      
