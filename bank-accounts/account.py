from argparse import ArgumentError, ArgumentTypeError
from dataclasses import asdict
from mimetypes import init


class Account:
    interestRate = 1.009
    numberOfAccounts = 0
    def __init__(self, balance, owner):
        if(balance < 0):
            raise Exception('Balance must be positive.')

        self.balance = balance
        self.owner = owner
        Account.numberOfAccounts += 1
    
    #methods for specific accounts
    def deposit(self, amount):
        if (amount>0):
            self.balance += amount
            print(f'Amount deposited: {amount}\nBalance now: {self.getBalance()}')

    def withdraw(self, amount):
        if amount<0:
            raise ValueError('Amount must be a positive number.')
        elif amount<=self.getBalance():
            raise ArgumentError('Withdraw amount cannot be larger than balance in account.')
        else:
            self.balance -= amount
            print('Amount withdrawn: {amount}\nBalance now: {self.getBalance()}')
    
    def addInterest(self):
        self.balance *= self.getInterestRate()
    
    def endYearUpdate(self):
        self.addInterest()

    # class-methods
    @classmethod
    def setClassInterestRate(cls, newInterestRate):
        cls.interestRate = newInterestRate

    #getters
    def getBalance(self):
        return self.balance

    def getOwner(self):
        return self.owner

    def getInterestRate(self):
        return self.interestRate

    #setters
    def setBalance(self, balance):
        self.balance = balance

    def setOwner(self, owner):
        if type(owner) != str:
            raise ArgumentTypeError('Owner must have a string as a name.')
        self.owner = owner
    
    def setInterestRate(self,  newInterestRate):
        if newInterestRate < 0 or (type(newInterestRate) != int and type(newInterestRate) != float) :
            raise ArgumentTypeError('Interest rate must be a positive integer or float.')
            # raise Exception('Interest rate must be positive.')
        self.interestRate = newInterestRate

def main():
    konto1 = Account(0, 'Per Hag')
    konto2 = Account(0, 'Kari Hag')
    konto2.setInterestRate(1.03)
    print(konto1.__dict__)
    print(Account.__dict__)
    print(konto2.__dict__)
    print(konto1.getInterestRate())
    print(konto2.getInterestRate())
    konto1.deposit(5000)
    konto1.addInterest()
    print(konto1.__dict__)
    Account.setClassInterestRate(1.02)
    print(konto1.getInterestRate())
    print(konto2.getInterestRate())
    print(konto1.__dict__)
    print(konto2.__dict__)
    konto3 = Account(2, 'Hans Inge')

main()

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

