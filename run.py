#!/usr/bin/env python3


from bank.user import User
from bank.account import Account


def create_account(account_number, balance, type):
	return Account(account_number, balance, type)

def create_user(name, account, pin_number):
	return User(name, account, pin_number)


stop = False

while stop is not True:
	print("What is your command?")
	print("1: Create an account")
	print("2: Log in to your account")
	print("3: Type \"stop\" to leave the bank")
	cmd = input()
	if cmd == "stop":
		stop = True
	elif cmd == "1":
		print("What is your name?")
		name = input()
		print("Choose your account number.")
		account = input()
		print("Choose your pin number.")
		pin_number = input()
		user = create_user(name, account, pin_number)
		print("Account created! Welcome, {}".format(user.name))

carter = User("Carter", 123, 1)
account = Account(123, 1000, "checking")

print("{} has account number {} with a pin number {}".format(carter.name, carter.account, carter.pin_number))
print("{} account with account number {} has balance {}".format(account.type, account.account_number, account.balance))

account.deposit(1000)
print(account.check_balance())
account.withdraw(500)
print(account.check_balance())
print("{} account with account number {} has balance {}".format(account.type, account.account_number, account.balance))
