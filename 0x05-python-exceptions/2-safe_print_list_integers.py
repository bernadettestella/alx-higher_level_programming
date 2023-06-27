#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
        except (ValueError, TypeError):
            pass
        else:
            c += 1
    print()
    return (c)
