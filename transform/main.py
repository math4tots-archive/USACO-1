def convert(chara):
    '''
    Takes '@' and converts it to 1
    Takes '-' and converts it to 0
    '''
    pass


def check(pattern, real, N):
    '''
    if the new pattern and the real pattern are the same then it
    returns True. Else, it will return False

    '''
    if pattern == real:
        return True


def lst_maker(N):
    '''
    Creates an empty list of N lists

    '''
    lst = []
    for x in range(N):
        lst.append([])
    return lst

def ninetydegrees(pattern, N):
    '''
    Pattern is a list of lists
    N is the number of rows/columns

    Creates list of lists that have been transformed
    90 degrees

    Returns T if this pattern is the same as the real product


    '''
    temp = lst_maker(N)
    for row in pattern:
        for i in range(len(row)):
            temp[i].append(row[i])
    new = []
    for t in temp:
        new.append(t[::-1])

    return new


def one_eighty(pattern, N):
    '''
    Does an additional 90 degrees to ninetydegrees(pattern, N)
    '''
    return ninetydegrees(ninetydegrees(pattern, N), N)

def two_seventy(pattern, N):
    return ninetydegrees(one_eighty(pattern, N), N)

def reflection(pattern, N):

    return list(reversed(pattern))

# assert reflection([[1, 0, 1], [0, 0, 0], [1, 1, 0]], 3) == [[1, 1, 0], [0, 0, 0], [1, 0, 1]], reflection([[1, 0, 1], [0, 0, 0], [1, 1, 0]], 3)

def combination(pattern, N):
    '''
    It takes the pattern and reflects it horizontally. Then it returns
    a new pattern that has been subjected to other transformation

    However, problem- There are three possible patterns that combination
    may produce.

    IDEA:
    Have a list that contains all of that. When at solve function, split this up
    specifically for combination
        -) Doesn't feel very efficient

    '''
    all_patterns = []
    new = reflection(pattern, N)
    all_patterns.append(ninetydegrees(pattern, N))
    all_patterns.append(one_eighty(pattern, N))
    all_patterns.append(two_seventy(pattern, N))

    return all_patterns


def solve(pattern, real, N):
    '''
    Checks to see if any of the combination creates
    an identical image as the real image.
    If so, return the corresponding pattern number
    Else, return invalid transtormation (#7)

    '''
    if pattern == real:
        return 6
    if check(ninetydegrees(pattern, N), real, N):
        return 1
    if check(one_eighty(pattern, N), real, N):
        return 2
    if check(two_seventy(pattern, N), real, N):
        return 3
    if check(reflection(pattern, N), real, N):
        return 4
    for pat in combination(pattern, N):
        if check(pat, real, N):
            return 5
    return 7


# THE FOLLOWING ARE PRODUCING BUGS!!
assert solve([[1, 0, 1]], [[0, 1, 1]], 1) == 7
assert solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]], 4) == 4, solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 0, 1, 0]], 4)







# assert solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]], 4) == 2, solve([[1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 0, 1]], [[1, 0, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]], 4)
# assert solve([[0]], [[0]], 1) == 7, solve([[0]], [[0]], 1)
# assert solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 0, 1], [1, 0, 0], [0, 0, 1]], 3) == 1, solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 0, 1], [1, 0, 0], [0, 0, 1]], 3)
# assert solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 1, 0], [0, 0, 0], [1, 0, 1]], 3) == 4, solve([[1, 0, 1], [0, 0, 0], [1, 1, 0]], [[1, 1, 0], [0, 0, 0], [1, 0, 1]], 3)















