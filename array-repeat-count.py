#!/usr/bin/env python

# Problem: given an array with repeated items, tell which one is the most
# repeated one
a = [1, 3, 4, 5, 3, 3, 2]

# Works on python < 3.0, for 3.0 and above the user must validate for None at
# line 19 or add a try except.
# This question was asked as "basic python".
b = dict()
for i in a:
    if b.get(i):
        b[i] += 1
    else:
        b[i] = 1

max = [None, None]
for k,v in b.iteritems():
    if max[1] < v:
        max = [k,v]

print max

# Better way:
from collections import Counter
z = Counter(a)
print z.most_common(1)
