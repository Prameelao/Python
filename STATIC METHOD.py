#usage of static method
class Bank:
    bank_name="sbi"
    ban_roi=7
    bank_branch="banglore"
    def __init__(self,n,a,b,ac):
        self.name=n
        self.age=a
        self.bal=b
        self.acount=a
    @classmethod
    def bank_details(cls):
        print(f"Bank name is {cls.bank_name}")
        print(f"Bank roi is {cls.bank_roi}")
        print(f"Bank branch is {cls.bank_branch}")
    def customer_details(self):
        print(f"customer name is {self.name}")
        print(f"customer age is {self.age}")
        print(f"customer balance is {self.bal}")
        print(f"customer acount is {self.acount}")
    @staticmethod
    def get_int_value():
        intv=int(input("enter a value"))
        return intv
    @staticmethod
    def get_str_value():
        sv=input("enter str value")
        return sv
    def withdraw(self):
        amount=self.get_int_value()
        if amount<=self.bal:
            self.bal=self.bal-amount
            print("withdraw is success")
            print("Balance is ",self.bal)
        else:
            print("insuffficiant balance")
    def Deposite(self):
        amount=self.get_int_value()
        if amount>0:
            self.bal+=amount
            print("withdraw is succeses present balance is",sel.bal)
        else:
            print("Plese enter amount greter than 0")
    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print("roi is modified")
    @classmethod
    def change_branch(cls):
        bb=cls.get_str_value()
        cls.bank_branch=bb
        print("branch name is changed ")
pramee=Bank("prameela",22,5000,12345)

Bank.change_branch()
    
































    
    
        
