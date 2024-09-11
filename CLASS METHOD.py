#Usage of Class Mathod
class Bank:
    bank_name="SBI"
    bank_ifsc=123
    bank_adress="Banglore"
    bank_rateofintrest=7
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.cage=ca
        self.cbal=cb
    @classmethod
    def modify_roi(cls):
        print("cls val is",cls)
        new=int(input("Enter a value"))
        cls.bank_rateofintrest=new
        print("roi changed now roi is",new)

shiva=Bank("shiva",22,5500)
Bank.modify_roi()
shiva.modify_roi()


