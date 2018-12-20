
def doomsdayDict(year, *args):
    doomsdayDict = {}
    for month in range(12):
        if year % 4 and year % 100 != 0 or year == 2000:
            if month == 0 or month == 1:
                doomsdayDict[month] = args[month] + 1
            else:
                doomsdayDict[month] = args[month]
        else:
            doomsdayDict[month] = args[month]

    return doomsdayDict

print(doomsdayDict(2000, 3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 17, 12))
print(doomsdayDict(1992, 3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 17, 12))







def findDoomsday(year):
    pass




def friday(end):
    pass

