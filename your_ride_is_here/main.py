"""
ID: jennife29
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

import string
from functools import reduce


def numbdict():
    numdict = {}
    count = 1
    for letter in string.ascii_uppercase:
        numdict[letter] = count
        count += 1
    return numdict


def ridehere(word):
    total = []
    for letter in word:
        total.append(numbdict()[letter])
    return reduce(lambda x, y: x*y, total)%47


word1 = fin.readline().strip()
word2 = fin.readline().strip()
if ridehere(word1) == ridehere(word2):
    fout.write(f"GO\n")
else:
    fout.write(f"STAY\n")



fout.close()








