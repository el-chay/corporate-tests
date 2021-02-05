#!/usr/bin/env python3
from math import sqrt, pow

def maxGameScore(cell):
    max_len = len(cell)+1
    # Get primes
    eratos = [True for i in range(0, max_len)]
    for i in range(2, int(sqrt(max_len))+1):
        if eratos[i]:
            c = 0
            j = int(pow(i,2))
            while j < max_len:
                eratos[j] = False
                c += 1
                j = int(pow(i,2))+c*i

    # Select jumps (primes ending in 3)
    i = 2
    jumps = [1,]
    while i < max_len:
        if eratos[i] and i%10 == 3:
            jumps.append(i)
        i += 1

    # Get the greater-than path
    i = 0
    sum = cell[0]
    possible_jumps = [(cell[i+j], i+j) for j in jumps if i+j < len(cell)]
    while i < len(cell) and len(possible_jumps) > 0:
        max_value, i = sorted(possible_jumps, key=lambda x: x[0])[-1]
        sum += max_value
        possible_jumps = [(cell[i+j], i+j) for j in jumps if i+j < len(cell)]
    return sum
