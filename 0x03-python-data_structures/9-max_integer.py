#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    greatest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > greatest:
            greatest = my_list[i]
    return (greatest)
