'''
ID: jennife29
LANG: PYTHON3
TASK: friday
'''
#The origin of the month is important


#"January" -> 1


def nmonth(y, m):
    if m in (9, 4, 6, 11):
        return 30
    elif m == 2:
        if leap(y):
            return 29
        else:
            return 28
    else:
        return 31

def leap(y):
    #if y % 4 != 0 is the same as if y % 4
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    else:
        return y % 4 == 0


def incr(y, m):
    """
    incr(2018, 1) == (2018, 2)
    incr(2018, 4) == (2018, 5)
    incr(2018, 12) == (2019, 1)
    """
    assert m in range(1, 13), m
    #m in range(1, 13) check | if it's wrong, then m would
    if m != 12:
        m += 1
    else:
        m = 1
        y += 1
    return y, m

def solve(N):
    d = (1900, 1)
    # r is the thing we're gonna return

    r = [0] * 7
    #Saturday = 0
    dow = 0 #day of week
    # Jan 13, 1900  => Saturday
    # Saturday = 0

    while d[0] < 1900 + N:
        r[dow] += 1
        # print(f"{d}, {r}, {nmonth(*d)}, {leap(d[0])}")
        dow += nmonth(*d)
        dow %= 7
        d = incr(*d)

    return r

f = open('friday.in')
# Don't have to write f.close()

with open('friday.in') as f:
    N = int(f.read())

answer = solve(N) #array
answerstr = " ".join(str(rep) for rep in answer)

with open("friday.out", "w") as f: #will default to "r" (read) instead of write
    f.write(f"{answerstr}\n")

# print(solve(5))









