#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError as ve:
        message = f"Exception: {ve}"
        sys.stderr.write(message)
        return (False)
    except TypeError as te:
        message = f"Exception: {te}"
        sys.stderr.write(message)
        return (False)
