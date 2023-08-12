#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5
result = (add(a, b), sub(a, b), mul(a, b), div(a, b))
if __name__ == "__main__":
    print("{0} + {1} = {2}".format(a, b, result[0]))
    print("{0} - {1} = {2}".format(a, b, result[1]))
    print("{0} * {1} = {2}".format(a, b, result[2]))
    print("{0} / {1} = {2}".format(a, b, result[3]))
