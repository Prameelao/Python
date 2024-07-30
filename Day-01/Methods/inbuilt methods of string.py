#LEN()
var='twygev884899#$%^&*'
print(len(var))
a='we are developera'
print(len(a))

#UPPER()
b='prameela'
print(b.upper())
b='Prameela'
print(b.upper())
b='PRAMEELA'
print(b.upper())
b='PRamEEla'
print(b.upper())

#LOWER
c='prameela oruGAntI'
print(c.lower())

#TITLE
d='prameela IS a gOOd girl'
print(d.title())

#CAPITALIZE
e='%56jesues loves me'
print(e.capitalize())

#COUNT(used to count the numer of characters of a specific char)
e='%56jesues loves me'
print(e.count('e'))
print(e.count('e',8,20))
print(e.count('e',8,17))

#REPLACE (used to replace the old char with new char)
f='am the child of jesues'
print(f.replace('c','d'))
print(f.replace('e','%',1))
print(f.replace('e','%',2))

#SWAP CASE(used to convert "uper to lower and lower to upper")
s='developERS'
print(s.swapcase())

#IS LOWER(it gives only boolean values has output)
s='2847GYTDUJIfdedreryh$%^&*'
print(s.islower())
s='ftuioedx 23@##$$%^^&456'
print(s.islower())

#IS UPPER(it gives only boolean values has output)
s='2847GYTDUJIfdedreryh$%^&*'
print(s.isupper())
s='DRTYIKH *%$@@^ 12233445'
print(s.isupper())

#IS TITLE
s='Am child of god'
print(s.istitle())
s='Am Child Of God 2345#%%^^'
print(s.istitle())

#ISCHAR
s='Am child of god'
print(s.isalpha())
s='Am Child Of God 2345#%%^^'
print(s.isalpha())
s='Amchildofgod'
print(s.isalpha())

#IS DIGIT
s='1233579'
print(s.isdigit())
s='1234 787'
print(s.isdigit())
s='2467%^^&**'
print(s.isdigit())
s='12345FDS hh'
print(s.isdigit())

#ISALNUM
s='1233579'
print(s.isalnum())
s='1234 787'
print(s.isalnum())
s='2467%^^&**'
print(s.isalnum())
s='12345FDS hh'
print(s.isalnum())
s='12345FDShh'
print(s.isalnum())

#ISSPACE
s='1233579'
print(s.isspace())
s='1234 787'
print(s.isspace())
s='2467%^^&**'
print(s.isspace())
s=''
print(s.isspace())
s='    '
print(s.isspace())

#INDEX(to find the index position)
var='god is always with you old'
#first occuarance o
print(var.index('o'))
m=var.index('o')
#second occurance of o
print(var.index('o',m+1))
print(var.index('o',var.index('o',m+1)+1))
print(var.index('a',0,16))

#RINDEX
z='Hello full future Engineers'
print(z.rindex('u'))
print(z.rindex('u',0,z.rindex('u')+1))


#STARTSWITH(gives T or F as output)
s='u5%uyfjgfjj'
print(s.startswith('u'))  #if it start with given letter then it give "true else false"
print(s.startswith('s'))
print(s.startswith('%'))
print(s.startswith('5'))

#ENDSWITH(gives T or F as output)
s='difgtihiifbo    '
print(s.endswith(''))
s='dhiewtuokkeiutuif'
print(s.endswith('f'))
print(s.endswith('5'))
print(s.endswith('^'))
print(s.endswith('s'))

















