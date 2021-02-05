#!/usr/bin/env python3
from math import sqrt, pow

def maxGameScore(cell):
    max_len = len(cell)+1
    # Get primes
    erastos = [True for i in range(0, max_len)]
    for i in range(2, int(sqrt(max_len))+1):
        if erastos[i]:
            c = 0; j = int(pow(i,2))+c*i
            while j < max_len:
                erastos[j] = False
                c = c+1
                j = int(pow(i,2))+c*i
    i = 2
    jumps = [1,]
    while i < max_len:
        if erastos[i] and i%10 == 3:
            jumps.append(i)
        i += 1

    i = 0
    sum = cell[0]
    while i < len(cell):
        possible_jumps = [(cell[i+j], i+j) for j in jumps if i+j < len(cell)]
        if len(possible_jumps) > 0:
            max_value, i = sorted(possible_jumps, key=lambda x: x[0], reverse=True)[0]
            sum += max_value
        else:
            break
    return sum
