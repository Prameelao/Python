#ADD inbuilt methods
#APPEND(adding single element to the list at the end)
L=[]
print(L.append(23))
print(L)
L.append("true")
print(L)
L.append([1,2,3])          #append can allow both "single & collection data"
print(L)
L.append((1,2,3))          #allows only one value it may be single or collection
print(L)
L.append({4,5})
L.append({'s':5,'r':6})
print(L)

#INSERT(to add single value at any where we want)
L=[1,2,3,56]
L.insert(0,88)
print(L)
L.insert(2,98)
print(L)
L.insert(100,500)           #if the index position is not available in that then the value can be added at "last"
L.insert(2,(235,678,789,))
print(L)

#EXTEND(add a collection of data type at the end of the list)
L=[]
L.extend("56")              #iterable means collection data
print(L)                    # if we give "collection data" but in output we will get "single values only"
L.extend([1,2,'s',[3,4],(5,6),{7,8}]) #if give collection data in side the collection data in output it will be in "collection data only"
L.extend((8,8,'str'))
print(L)
L.extend({'s':6,'m':7})    #if give dictionary in output only "key values" can be represents
print(L)



#REMOVING inbuilt methods
#REMOVE
L=[1,2,'str',6,79,8,{1,2},(3,4),[12,33]]     #if the value not avilable in list it throws an error like "x not in list"
L.remove('str')
L.remove(2)
L.remove([12,33])
print(L)

#CLEAR(removes all elements in list)
L=[1,2,'str',6,79,8,{1,2},(3,4),[12,33]]
L.clear()
print(L)
var='hello'
print(var.count('n'))

#discard
#L=[1,2,'str',6,79,8,{1,2},(3,4),[12,33]]    list doesnt have the "DISCARD" inbilt method
#L.discard('str')
##L.discard('pr')
#print(L)

#INDEX
L=[1,2,'str',6,2,79,8,{1,2},2,(3,4),[12,33]]
print(L.index(2))
print(L.index(2,L.index(2)+1))
print(L.index(2,L.index(2,L.index(2)+1)+1))

#SORT
L=[7,9,889742,9,45]
L.sort(reverse=True)
print(L)
L.sort(reverse=False)
print(L) 
var=[33,22,88,55,11,10000]                     #it can be used for only on "LIST" return type is "NONE"
print(var.sort(reverse=True))
print(var)
print(var.sort(reverse=False))
print(var)

#SORTED
var=[5,6,9,3,8,58]                             #works on collection data types return type is "LIST"
print(sorted(var))
print(sorted(var,reverse=True))
print(sorted(var,reverse=False))

#JOIN
a=['1','23', '4',]
print(a)
print('ryrfh'.join(a))
b='strui'
print('#$7'.join(a))
c=['str','pr','56']
print('*'.join(c))

#COPY
a=['1','23', '4',]
print(id(print(a.copy())))   #copy the value in other memory location
print(id(a))

#count
a=['1','23', '4',1,1,1]
print(a.count(1))
print(a.count(5))
print(a.count('23'))

#MAX
a=[234,789,987,]
print(max(a))

#MIN
a=[234,789,987,]
print(min(a))
b=['a','n','u','k','p'',d']
print(min(b))






















































