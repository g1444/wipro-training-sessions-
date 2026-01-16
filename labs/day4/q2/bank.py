class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def withdraw(self,amount):
        try:
            if amount> self.balance:
                raise ValueError("Insufficient balance")
            elif amount<=0:
                raise ValueError("invalid input")
            else:
                self.balance-=amount
                print("remaining balance :",self.balance)
        except Exception as e:
            print("withdrawl failed",e)
    def deposit(self,amount):
        try :
            if amount<=0:
                raise ValueError("deposit must be graater than 0")
            self.balance+=amount
            print(f"deposit of {amount} successful")
            print(f"remaining balance :{self.balance}")
        except Exception as e:
            print("deposit failed",e)
    def _del__(self):
        print("transaction successful")

acc=BankAccount(102,2400)
acc.deposit(2000)
acc.withdraw(200)