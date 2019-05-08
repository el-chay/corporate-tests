#!/usr/bin/env python
def fib(i):
    def bif(i, a, b):
        print i, a, b
        if i == 0:
            return a
        else:
            return bif(i-1, b, a+b)
    return bif(i, 0, 1)
