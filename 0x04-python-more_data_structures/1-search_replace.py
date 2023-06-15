#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if y == search else y for y in my_list]
