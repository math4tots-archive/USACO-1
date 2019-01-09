def convert():
    '''
    Takes '@' and converts it to 1
    Takes '_' and converts it to 0
    '''
    pass


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

    Returns a list of lists that have been transformed
    90 degrees
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

def check(pattern, real, N):
    '''
    Checks to see if any of the combination creates
    an identical image as the real image.
    If so, return the corresponding pattern number
    Else, return invalid transtormation (#7)

    '''
    pass












