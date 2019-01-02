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
    return f"{max(continuous)} {max(stop)}"






N = int(input())
times = []
for n in range(N):
    time = [int(x) for x in input().split()]
    times.append(time)
# print(cont_times(times))
print(longest(cont_times(times)))



