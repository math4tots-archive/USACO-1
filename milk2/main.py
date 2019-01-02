def merge():
    pass

def possible(times):
    total = []
    for i in range(len(times) - 1):
        result = merge(times[i], times[i + 1])
        if result:
            total.append(result)
        else:
            total.append(time[i])



def filter():
    pass

def dict_lst():
    pass