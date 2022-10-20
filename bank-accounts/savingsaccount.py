from account import Account


class SavingsAccount(Account):
    interestRate = 1.05

saving1 = SavingsAccount(0,'Jon Sverre')
saving2 = SavingsAccount(60000,'Scrooge Ebeneizer')
saving1.setInterestRate(1.06)

class BSU(SavingsAccount):
    pass

print(saving1.__dict__)
print(saving2.__dict__)
print(saving2.getInterestRate())

