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
        # print(times[i], times[i + 1])
        # print(separate)
        if separate:
            #I might be able to replace separate with combined (ex. if combined instead)
            overlap = merge(times[i], times[i + 1])
            # print(f"{i} round and overlap {overlap}")
            if overlap:
                separate = False
                for t in overlap:
                    combined.append(t)
        else:
            print(times[i], times[i + 1])
            overlap = merge(combined, times[i + 1])
            print(f"overlap {overlap}")
            if overlap:
                separate = False
                del combined[-1]
                combined.append(overlap[1])
        if not overlap:
            separate = True
            sideline = [times[i], times[i + 1]
            milk.append(combined)
            #This is submitting in [300, 1200]

    if combined not in milk:
        milk.append([combined])

    return milk




ntimes = []
N = int(input())
for n in range(N):
    farm = [int(x) for x in input().split()]
    ntimes.append(farm)

from operator import itemgetter
times = sorted(ntimes, key=itemgetter(0))
print(milking(times))





            # else:
            #     milk.append(combined)
            #     separate = False
                #I'm not sure about the above









