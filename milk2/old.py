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

