#SET INBUILT METHODS
#ADD() (to add single value to the set)
a={'q',7,'str',(1,2)}
print(a.add(40,))
print(a)
a.add(('a','b',(1,2)))
print(a)

#UPDATE (to add multiple values to the set)
b={'s',8,(1,2),4.5,True,False,0}
b.update('strm[1,2](4,3){5,6}67')
print(b)
c={'n',(1,2,3),4.5,True,5}
c.update([2,4.5,4+5j,True,'str',(3,4)])
print(c)
d=set()
d.update((1,2,(3,4),True))
print(d)
d.update({41,26})
print(d)
d.update({'s':1,'d':2})
print(d)

#REMOVE
s={3,3.4,True,(1,2),'pramee'}
print(s.remove(3))                          #if the value is not available then remove method gives "ERROR"
print(s)

#DISCARD
s={0,2.3,True,(3,4),'str'}
s.discard(0)
s.discard(500)                              #if the given value not available then discard method gives "NONE"
print(s)


#CLEAR
s={1,(89,905,),'2m3'}
print(s.clear())
print(s)

#POP
s={2,4.5,True,3+2j,(4,5,6),'ste'}
print(s.pop())
print(s.pop())                              #if all values are clera then pop method gives "ERROR"
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

#UNION
a={'str',(3,4,5),(6,7,3)}
b={'prs',(4,5),'str'}
print(a.union(b))
print(a.union(a))
print(b.union(b))
print(b.union(a))

#INTERSECTION
a={'str',(3,4,5),(6,7,3)}
b={'prs',(4,5),'str'}
print(a.intersection(b))
print(a.intersection(a))
print(b.intersection(b))
print(b.intersection(a))


#DIFFERENCE
a={'str',(3,4,5),(6,7,3)}
b={'prs',(4,5),'str'}
print(a.difference(b))
print(b.difference(a))
print(a.difference(a))
print(b.difference(b))

#ISDISJOINT
a={'str',(3,4,5),(6,7,3)}
b={'prs',(4,5),'str'}
print(a.isdisjoint(b))
a={'str',(3,4,5),(6,7,3)}
b={'prs',(4,5)}
print(a.isdisjoint(b))

















































