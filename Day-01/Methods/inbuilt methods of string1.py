#CENTER()
a='Pramee is a good girl'
print(len(a))
print(a)
print(a.center(30,'@'))
#print(a.center())                    atleast 1 argument is mandatory
#print(a.center('@'))                 width is must
print(a.center(30,))
s=a.center(60,'*')
print(len(s))
print(s)
print(a.center(2,'@'))

#MAX()
b='38775678'
print(max(b))
b='hkbdkzZ'
print(max(b))

#MIN()
b='38775678'
print(min(b))
b='cbhkbdkzZ'
print(min(b))

#CASEFOLD
s='pramee@ &**%02002'
print(s.casefold())
##s='pramee@ &**%02002'
print(s.lower())
s='ss'
print(s.lower())

#EXPANDTABS
a='h\te\tl\tl\to'
print(len(a))
print(a)
print(a.expandtabs(1))
print(len(a.expandtabs(1)))
print(a.expandtabs(2))
print(len(a.expandtabs(2)))
print(a.expandtabs())

#ISIDENTIFIER
s='str'
print(s.isidentifier())
s='ry396'
print(s.isidentifier())
s='pramee_'
print(s.isidentifier())
s='78pramee'
print(s.isidentifier())
s='_pramee'
print(s.isidentifier())
s='and'
print(s.isidentifier())
s='pramee_@2002'
print(s.isidentifier())
s='pramee 2002'
print(s.isidentifier())
s='pramee_2002'
print(s.isidentifier())

#ISNUMERIC
s='1344'
print(s.isnumeric())
s='124ab'
print(s.isnumeric())
s='5.5'
print(s.isnumeric())
s='31.67'
print(s.isnumeric())
s='八'                    #chinise value 8
print(s.isdigit())
print(s.isnumeric())
s='\u0030'                #unicode for "zero"
print(s.isnumeric())


#ISPRINTABLE
a='hello\n are you#1?'
print(a)
print(a.isprintable())
a='hello are you#1?'
print(a.isprintable())

#ISASCII
a='pramee123'
print(a.isascii())
a=' á, or ñ'
print(len(a))
print(a.isascii())
b='abcABC123'
print((b.isascii))
b='abcABC123'
print((b.isascii))

#STRIP
a='pramee is good girl'
print(a.strip())
a='    pramee is good girl    '
print(a.strip())
a=',,,,.....rrrr pramee....,,,,,,rrrr'
print(a.strip(',r'))

#LSTRIP
a='pramee is good girl'
print(a.lstrip())
a='    pramee is good girl    '
print(a.lstrip())
a=',,,,.....rrrr pramee....,,,,,,rrrr'
print(a.lstrip(',.r'))

#RSTRIP
a='pramee is good girl'
print(a.rstrip())
a='    pramee is good girl    '
print(a.rstrip())
a=',,,,.....rrrr pramee....,,,,,,rrrr'
print(a.rstrip(',.r'))

#RSPLIT
s='pramee is a good girl'
print(s.split())
s='pramee is a goaod giarl'
print(s.split('a',2))
s='pramee is a goaod giarl'
print(s.rsplit('a',2))


#PARTITION
s='pramee good is a good girl'
print(s.partition('good'))
#s='pramee is a good girl'
#print(s.partition())
#s='pramee is a good girl'
#print(s.split('good','girl'))
#s='pramee is a good girl'
#print(s.partition(2))

#RPARTITION
s='pramee good is a good girl'
print(s.rpartition('good'))

#LJUST
s='pramee'
print(s.ljust(10))
s='pramee'
print(s.ljust(10,'*'))
#s='pramee'
#print(s.ljust())
#s='pramee'
#print(s.ljust('*'))

#RJUST
s='pramee'
print(s.rjust(10))
s='pramee'
print(s.rjust(10,'*'))

#JOIN
a=("pramee","oruganti","ammu")
print("#".join(a))

#ZFILL
a='pramee'
print(a.zfill(10))
a='pramee'
print(a.zfill(5))











































