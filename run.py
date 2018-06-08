#!/usr/bin/env python3

from bank.user import User

carter = User("Carter", 123, 1)

print("{} has account number {} with a pin number {}".format(carter.name, carter.account, carter.pin_number))
