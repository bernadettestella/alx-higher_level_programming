#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        f = add(a, b)
        for n in range(4, 6):
            f = add(f, n)
        return f

    else:
        return (sub(a, b))
