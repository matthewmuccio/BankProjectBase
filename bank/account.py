#!/usr/bin/env python3

class Account:
	def __init__(self, account_number, balance, type):
		self.account_number = account_number
		self.balance = balance
		self.type = type

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

	def check_balance(self):
		return self.balance
