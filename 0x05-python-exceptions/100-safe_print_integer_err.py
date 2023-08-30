#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        error_message = "Exception: Unknown format code 'd' for object of type 'str'"
        sys.stderr.write(error_message)
        return (False)
    except TypeError:
        error_message = "Exception: Unknown format code 'd' for object of type 'str'"
        sys.stderr.write(error_message)
        return (False)
