'''
Attempt 4
'''
def check(times):
    for i in range(len(times) - 1):
        if merge(times[i], times[i + 1]):
            return True
    return False

def cont_times(times):
    ntimes = times
    while check(ntimes):
        ntimes = filter(possible(ntimes))
    return ntimes


def merge(time1, time2):
    if time1[1] >= time2[0]:
        if time1[1] > time2[1]:
            return [time1[0], time1[1]]
        else:
            return [time1[0], time2[1]]
    else:
        return []

def dict_lst(sieve):
    temp = []
    dictList = []
    # print(sieve)
    for key, value in sieve.items():
        temp = [key, value]
        dictList.append(temp)
    return dictList


def possible(times):
    total = []
    for i in range(len(times) - 1):
        result = merge(times[i], times[i + 1])
        # print(result)
        if result:
            total.append(result)
        else:
            total.append(times[i])
    if times[len(times) - 1] not in total:
        total.append(times[len(times) - 1])
    return total

def filter(total):
    sieve = {}
    for t in total:
        if t[1] in sieve:
            if t[0] < sieve[t[1]]:
                sieve[t[1]] = t[0]
        else:
            sieve[t[1]] = t[0]
    return dict_lst({v: k for k, v in sieve.items()})


def longest(cont):
    continuous = []
    for length in cont:
        continuous.append(length[1] - length[0])
    stop = []
    for i in range(len(cont) - 1):
        stop.append(cont[i + 1][0] - cont[i][1])
    if stop == []:
        stop = [0]
    return f"{max(continuous)} {max(stop)}"


N = int(input())
times = []
for n in range(N):
    time = [int(x) for x in input().split()]
    times.append(time)

# print(cont_times(times))
print(longest(cont_times(times)))










'''
Attempt 3
'''
def merge(time1, time2):
    '''
    Checks to see if time2 is in time1.
    if yes:
        return merged list
    else:
        return an empty list
    Requires:
        1 if/else statement
    '''
#What happens if then next list2[1] is smaller than  list1[1]
    # print([time1[0], time2[1]])
    if time1[1] >= time2[0]:
        return [time1[0], time2[1]]
    else:
        return []


def milking(times):
    '''
times = already been sorted
Should return a list of lists of continuous times (milk)
Should require:
    2 for loop
    3 if/else statement


    '''

    separate = True
    combined = []
    milk = []
    for i in range(len(times) - 1):
        if separate:
            #I might be able to replace separate with combined (ex. if combined instead)
            overlap = merge(times[i], times[i + 1])
            if overlap:
                separate = False
                for t in overlap:
                    combined.append(t)
        else:
            overlap = merge(combined, times[i + 1])
            if overlap:
                separate = False
                del combined[-1]
                combined.append(overlap[1])
        if not overlap:
            separate = True
            milk.append(combined)
            #This is submitting in [300, 1200]

    if combined not in milk:
        milk.append([combined])

    return milk
    # if sideline:
    #     for s in sideline:
    #         if any(sideline[s][1] not in sublist for sublist in milk):
    #             milk.append(sideline[s])



'''
Attempt 2
'''

def compare(stimes):
    pass



def cont_Times(times):
    from operator import itemgetter
    stimes = sorted(times, key=itemgetter(0))
    cont = []
    start = 0
    end = 10**9
    for i in range(len(stimes) - 1):
        print(f"start {start} end {end}")
        if stimes[i][1] == end:
            if stimes[i][1] >= stimes[i + 1][0]:
                start = stimes[i][0]
                end = stimes[i + 1][1]
            else:
                cont.append([start, end])
            continue
        if stimes[i][1] < stimes[i + 1][0]:
            print(f"{stimes[i]}")
            if end != 10**9:
                cont.append([start, end])
            start = stimes[i + 1][0]
            end = stimes[i + 1][1]

        if stimes[i][1] >= stimes[i + 1][0]:
            start = stimes[i][0]
            end = stimes[i + 1][1]
    if end not in cont:
        cont.append([start, end])
    return cont



def diff(cont):
    '''
    Subtract lst[1] with lst[0] and put into a list of difference.
    Spits out the max difference

    '''
    pass




times = []
N = int(input())
for n in range(N):
    farm = [int(x) for x in input().split()]
    times.append(farm)
print(cont_Times(times))



'''
Attempt 1
ID: jennife29
LANG: PYTHON3
TASK: milk2
'''


def milk_time(times):
    '''
    times = [[a, b], [a, b], [a, b]]

    '''
    a = 300
    b = 10**6
    longest = [0, 0]
    for time in times:
        if a <= time[0] < b:
            b = time[1]
            longest[0] = b - a
        else:
            if time[0] > b:
                longest[1] = time[0] - b
    return " ".join(str(t) for t in longest)

with open('milk2.in') as f:

    N = int(f.readline())
    times = []
    for n in range(N):
        farm = [int(x) for x in f.readline().strip().split()]
        times.append(farm)


with open("milk2.out", "w") as f:
    f.write(f"{milk_time(times)}\n")

