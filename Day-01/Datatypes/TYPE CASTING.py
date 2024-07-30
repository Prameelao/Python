#TYPE CASTING(converting from one data type to another data type)
#converting INT
print(int(5))
print(int(5.0))
print(int(5.9))
print(int(True))
print(int(False))
#print(int(1+2j))
#print(int('123'))
#print(int('25.6'))     it allows only FLOAT,BOOLEAN,AND STRING WITH integers
#print(int('abc'))
#print(int('35ygj'))
print(int())

#converting into FLOAT
print(float(5))
print(float(5.5))
print(float(True))
print(float(False))
#print(float(2+3j))
print(float('123'))               #argument must be a string or a real number, not 'list'
#print(float('abc'))
#print(float('245abc'))
#print(float([1,2,3]))
print(float())

#converting to BOOLEAN
print(bool(25))
print(bool(0))
print(bool(None))
print(bool(''))                 #it gives "TRUE" for all "true values"
print(bool(0.0))                #it gives "FALSE" for all "false values"
print(bool([]))
print(bool({}))
print(bool(set()))
print(bool(()))
print(bool(2.5))
print(bool(True))
print(bool(False))
print(bool('str'))
print(bool([1,2,3]))
print(bool((1,2)))
print(bool({1,2}))
print(bool({'s':1,'n':2}))
print(bool())

#convering int COMPLEX
print(complex())
print(complex(2))
print(complex(3,5))
print(complex(2+3j,3))
print(complex(5,6+7j))          #it allows two arguments
#print(complex('str',5))        #it allows all single value data types and string with integers
#print(complex(5,'str'))
print(complex('234'))
#print(complex('12ab'))
#print(complex([1,2,3]))


#converting into "STRING"
print(str(5))
print(str(True))
print(str(6.5))
print(str(3+2j))
print(str([1,2,'str',True,5.5,[3,4],(5,6),{1,2},{'a':8,'b':7}]))
c=[1,2,'str',True,5.5,[3,4],(5,6),{1,2},{'a':8,'b':7}]
print(len(c))
print(len(str([1,2,'str',True,5.5,[3,4],(5,6),{1,2},{'a':8,'b':7}])))
print((str((2,34,56))))
print(len(str((2,34,56))))
print(str({2,3,4,5,5,6}))
print(len(str({2,3,4,5,5,6})))
print((str({'a':1,'b':3})))
print(len(str({'a':1,'b':3})))

#converting to "LIST"
#print(list(4))            we can't convert a 'single value data' into list
print(list('abs460&^^'))
#print(list((1)))         #without comma tuble considerd as a integer
print(list((1,2,True,'str',[2,3],(5,6),{7,8},{'a':4,'b':8})))
print(list({1,2,True,'str',(5,6)}))
print(list({'a':3,'b':5,(1,2,3):6}))

#converting into "TUPLE"
#print(tuple(5))              tuple also allows only 'collection data'
print(tuple('a'))
print(tuple('pramee is a doog girl @2002'))
print(tuple([1,2,True,5.6,'str',[1,2,'str',True,5.5,[3,4],(5,6),{1,2},{'a':8,'b':7}]]))
print(len(tuple([1,2,True,5.6,'str',[1,2,'str',True,5.5,[3,4],(5,6),{1,2},{'a':8,'b':7}]])))
print(tuple({1,3,5,6}))
print(tuple({'a':1,'b':3}))
print(tuple())


#converting to SET
#print(set(5))     it allows only collection data
print(set('pramee'))
print(set([2,3,5]))
#print(set([2,3,5,[5,6]]))
print(set((4,5,'str')))
print(set({3,6}))
print(set({'a':1,'b':6}))




























