#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    my_list_set = set(my_list)
    for i in my_list_set:
        result += i
    return (result)
