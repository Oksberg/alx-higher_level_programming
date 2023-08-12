#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden_4_attr = dir(hidden_4)
    for attribute in hidden_4_attr:
        if not attribute.startswith("__"):
            print("{}".format(attribute))
