def determineDay(year):
    alldays = {}
    for d in range(7):
        alldays[d] = 0

    for y in range(1900, year):
        for m in range(12):
            diff = abs(doomsdayDict(y)[m] - 13)
            final = findDoomsday(y) + diff
            while final > 6:
                final -= 7
            alldays[final] += 1

    return alldays
