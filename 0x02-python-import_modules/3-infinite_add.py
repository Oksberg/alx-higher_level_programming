#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_of_args = len(sys.argv)
    result = 0

    for i in range(num_of_args - 1):
        num = int(sys.argv[i + 1])
        result += num

    print(result)
