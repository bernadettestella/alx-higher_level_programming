#!/usr/bin/python3
def add_tulpe(tulpe_a(), tulpe_b()):
    a, b = len(tulpe_a), len(tulpe_b)
    new_tulpe = ((tulpe_a[0] if a >= 1 else 0) + (tulpe_b[0] if b >= 1 else 0),
                 (tulpe_a[1] if a >= 2 else 0) + (tulpe_b[1] if b >= 2 else 0))

    return new_tulpe
