#!/usr/bin/env python3

from bank.user import User
from bank.account import Account

carter = User("Carter", 123, 1)
account = Account(123, 1000, "checking")

print("{} has account number {} with a pin number {}".format(carter.name, carter.account, carter.pin_number))
print("{} account with account number {} has balance {}".format(account.type, account.account_number, account.balance))

account.deposit(1000)
print(account.check_balance())
account.withdraw(500)
print(account.check_balance())
print("{} account with account number {} has balance {}".format(account.type, account.account_number, account.balance))
