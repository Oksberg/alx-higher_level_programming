#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_of_args = len(sys.argv)
    if num_of_args == 1:
        print("0 arguments.")
    elif num_of_args == 2:
        print("{} argument:".format(num_of_args - 1))
        print("{}: {}".format(num_of_args - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(num_of_args - 1))
        for i in range(num_of_args - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
