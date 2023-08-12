#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":

    num_of_args = len(sys.argv)
    if num_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operators = ['+', '-', '*', '/']
    operator = sys.argv[2]

    if operator in operators:
        if operator == '+':
            result = calculator_1.add(a, b)
        elif operator == '-':
            result = calculator_1.sub(a, b)
        elif operator == '*':
            result = calculator_1.mul(a, b)
        elif operator == '/':
            result = calculator_1.div(a, b)
        print("{} {} {} = {}".format(a, operator, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
