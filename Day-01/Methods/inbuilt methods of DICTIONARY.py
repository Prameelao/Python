#to add a SINGLE KEY VALUE PAIR
var={}
var['s']=5
print(var)
var[(1,2,3)]=8
print(var)
var[3+3j]=9
print(var)

#UPDATE(used to add "MULTIPLE ELEMENTS")
a={}
a.update(['sr',(4,6)])
print(a)
a.update([[(1,3),2],'pr'])
print(a)

#POP
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.pop('a'))
print(a)
print(a.pop((3,4)))
print(a)

#POPITEM
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.popitem())
print(a.popitem())
print(a.popitem())                     #we cant perform a popitem on EMPTY DICTIONARY it gives an ERROR
print(a.popitem())
#print(a.popitem())

#GET
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.get('a'))
print(a.get('name'))
print(a.get('name',500))
print(a)

#SETDEFAULT
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.setdefault('a'))
print(a.setdefault('name'))
print(a.setdefault('name',500))
print(a)

#KEYs
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
#print(a.keys('a'))  no need of argument
print(a.keys())

#VALUES
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.values())

#ITEMS
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.items())

#FROMKEYS
print({}.fromkeys('uioruhd'))
print({}.fromkeys('ueyhri',500))
print({}.fromkeys((1,2,(5,7))))
print({}.fromkeys([1,2,(5,7)],500))
print({}.fromkeys({1,2,(5,7)},1000))
print({}.fromkeys({'a':5,'pramee':'name','age':20,(3,4):'str'}))

#CLEAR
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(a.clear())
print(a)

#COPY
a={'a':5,'pramee':'name','age':20,(3,4):'str'}
print(id(a.copy()))
print(id(a))









































