#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()

    for y, z in new_dictionary:
        new_dictionary[y] = z * 2

    return new_dictionary
