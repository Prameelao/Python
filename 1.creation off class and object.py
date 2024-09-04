#creation of Class and Object
##class sample():
##    var1=10
##    var2=20
##    var3=70
##obj1=sample()
##print(sample.var1) #using class accessing
##print(sample.var2)
##print(obj1.var1) #using object accessing

##obj1.var1=40     #modifying using object
##print(sample.var1)
##print(obj1.var1)

##sample.var1=40     #modifying using class
##print(sample.var1) 
##print(obj1.var1)

##del sample.var1    #deleting using class
##print(sample.var2)
##print(obj1.var1)
##
##del obj1.var1
####print(sample.var1)
##print(obj1.var1)


class bank():
    bank_name='SBI'
    bank_ifsc=2677
    bank_address='Nellore'
pramee=bank()
print(bank.bank_address)# Accessing generic property by using CLASS
bank.bank_adress="Marripadu"
print(bank.bank_adress)

##print(pramee.bank_adress) #Accessing generic property by using OBJECT
##del bank.bank_name    #deleting generic property by using CLASS
##print(bank.bank_name)
del pramee.bank_ifsc
print(bank.bank_ifsc)




