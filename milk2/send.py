'''
ID: jennife29
LANG: PYTHON3
TASK: milk2
'''


def overlap(time1, time2):
    if time1[1] >= time2[0]:
        return True
    else:
        return False

def merge(time1, time2):
    if time1[1] > time2[1]:
        return [time1[0], time1[1]]
    else:
        return [time1[0], time2[1]]


def merge_intervals(old_intervals):
  ret = []
  for interval in old_intervals:
     if ret and overlap(ret[-1], interval):
         ret[-1] = merge(ret[-1], interval)
     else:
         ret.append(interval)
  return ret

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



with open('milk2.in') as fin, open("milk2.out", 'w') as fout:
    utimes = []
    N = int(fin.readline())
    for n in range(N):
        time = [int(x) for x in fin.readline().strip().split()]
        utimes.append(time)
    from operator import itemgetter
    old_intervals = sorted(utimes, key=itemgetter(0))
    fout.write(f"{longest(merge_intervals(old_intervals))}\n")





