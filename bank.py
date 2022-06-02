# Add these methods to class Account - deposit, withdraw. Create
# two instances of account and verify they work as expected.

class Bank:
    bank_account="Equity"
    def __init__ (self,accountname,name,balance,deposit,withdraw):
        self.name=name
        self.accountname=accountname
        self.balance=balance+deposit-withdraw
        self.deposit=deposit
        self.withdraw=withdraw

    def greet(self):
        return f"Hello {self.name}, your accountname is {self.accountname},you have deposited {self.deposit}, withdrawn {self.withdraw} and your balance {self.balance}"
       