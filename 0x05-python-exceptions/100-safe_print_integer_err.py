#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        message = "Exception: Unknown format code 'd' for object of type 'str'"
        sys.stderr.write(message)
        return (False)
    except TypeError:
        message = "Exception: Unknown format code 'd' for object of type 'str'"
        sys.stderr.write(message)
        return (False)
