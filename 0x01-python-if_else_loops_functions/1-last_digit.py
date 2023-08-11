#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print("{0} {1} {2} {3} {status[0]}".format("Last digit of", number, "is", last_digit, status = ("and is greater than 5", "and is 0", "and is less than 6 and not 0")))
elif last_digit == 0:
    print("{0} {1} {2} {3} {status[1]}".format("Last digit of", number, "is", last_digit, status = ("and is greater than 5", "and is 0", "and is less than 6 and not 0")))
elif last_digit > 6 and last_digit != 0:
    print("{0} {1} {2} {3} {status[2]}".format("Last digit of", number, "is", last_digit, status = ("and is greater than 5", "and is 0", "and is less than 6 and not 0")))
