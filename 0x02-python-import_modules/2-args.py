#!/usr/bin/python3
import sys

num_of_args = len(sys.argv)
if num_of_args == 1:
    if __name__ == "__main__":
        print("0 arguments.")
else:
    print("{} arguments:".format(num_of_args - 1))
    for i in range(num_of_args - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
