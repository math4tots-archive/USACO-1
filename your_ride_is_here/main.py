"""
ID: jennife29
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
x,y = map(int, fin.readline().split())
sum = x+y
fout.write (str(sum) + '\n')
fout.close()


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


# word1 = input()
# word2 = input()
# if ridehere(word1) == ridehere(word2):
#     print("GO")
# else:
#     print("STAY")
#










