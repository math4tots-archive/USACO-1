
'''
ID: jennife29
LANG: PYTHON3
TASK: beads
'''




from collections import deque
#double ended queue
#like a list but can easily add/remove at the beginning (and at the end)
#Each cutting point (linear) * a bead so N^2


def matching_colors(a, b):
    if 'w' in (a,b):
        return True
    else:
        return a == b

def combined_color(a,b):
    if a == 'w':
        return b
    elif b == 'w':
        return a
    else:
        assert a == b, (a,b)
        return a

def count(cut_necklace):
    total = 0
    left = 'w'
    right = 'w'

    #take from left side
    while cut_necklace and matching_colors(left, cut_necklace[0]):
        bead = cut_necklace.popleft()
        left = combined_color(left, bead)
        total += 1

    while cut_necklace and matching_colors(right, cut_necklace[-1]):
        bead = cut_necklace.pop()
        right = combined_color(right, bead)
        total += 1

    return total

def cut(necklace, pos):
    return deque(necklace[pos:] + necklace[:pos])

def solve(necklace):
    return max(count(cut(necklace, p)) for p in range(len(necklace)))


with open('beads.in') as fin, open("beads.out", 'w') as fout:
    fin.readline()
    necklace = fin.readline().strip()
    fout.write(f"{solve(necklace)}\n")










