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
  return


