'''
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







#Maybe I can make a max(generator)?