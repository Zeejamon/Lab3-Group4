import pickle
import random

from bank import Bank
from savingsaccount import SavingsAccount

bank = Bank()

bank.add(SavingsAccount("Tupaz","2133",5000.00))
bank.add(SavingsAccount("Celadina","1223",4000.00))
bank.add(SavingsAccount("Abella","4320",3500.00))
bank.add(SavingsAccount("Gonzales","6969",2000.00))
bank.add(SavingsAccount("Santiago","1002",1532.00))
bank.add(SavingsAccount("Paco","5411",1234.00))
bank.add(SavingsAccount("Ga Che","6432",1500.00))
bank.add(SavingsAccount("Pastrana","7211",1700.00))

print(bank)