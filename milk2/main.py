def compare(times):
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
print(compare(times))