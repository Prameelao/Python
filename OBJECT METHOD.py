#usage of object method
class Bank:
    bank_name="sbi"
    bank_ifsc=124
    bank_branch="kizkistan"
    def __init__(self,cn,cac,cb):
        self.cname=cn
        self.caccount=cac
        self.cbalance=cb
    def customer_details(self):
        print(f'Name of the customer Name {self.cname}')
        print(f"customer account number {self.caccount}")
        print(f'customer balance {self.cbalance}')
    def withdraw(self):
        amount=int(input("Enter amount"))
        if self.cbalance>=amount:
            print("Withdraw is Successful",self.cbalance-amount)
        else:
            print("Insufficiant Fonds")
    def Deposite(self):
        amount=int(input("Enter amount"))
        if amount>0:
            self.cbalance=self.cbalance+amount
            print("deposite is successful",self.cbalance)
        else:
            print("please enter the amount more than ZERO")
pramee=Bank("Prameela",767489,50000)
pramee.customer_details()
pramee.withdraw()
pramee.Deposite()

