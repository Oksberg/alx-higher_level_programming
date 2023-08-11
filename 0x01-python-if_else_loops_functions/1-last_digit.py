#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
output_string = "Last digit of {} is {} {}"
status = ("and is greater than 5", "and is 0", "and is less than 6 and not 0")
if number < 0:
    last_digit = -(abs(number) % 10)
else:
    last_digit = number % 10
if last_digit > 5:
    print(output_string.format(number, last_digit, status[0]))
elif last_digit == 0:
    print(output_string.format(number, last_digit, status[1]))
elif last_digit < 6 and last_digit < 0:
    print(output_string.format(number, last_digit, status[2]))
