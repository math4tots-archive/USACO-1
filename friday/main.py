def isLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True



def doomsdate(year):
    dooms =[3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 17, 12]
    doomsdate = {}
    for month in range(12):
        if isLeap(year):
            if month == 0 or month == 1:
                doomsdate[month] = dooms[month] + 1
            else:
                doomsdate[month] = dooms[month]
        else:
            doomsdate[month] = dooms[month]

    return doomsdate

# print(doomsdate(2001))
# print(doomsdate(1900))
# print(doomsdate(1911))


def centuryCode(year):
    year //= 100
    century = [3, 2, 0, 5]
    code = year - 19
    while code > 3:
        code -= 4
    return century[code]

# print(centuryCode(year)


def findDoomsday(year):
    important = [centuryCode(year)]
    decade = year % 100
    num1 = decade // 12
    remain1 = decade % 12
    if num1 != 0:
        num2 = remain1 // num1
    else:
        num2 = 0
    important.extend([num1, remain1, num2])
    total = sum(important)
    if total > 6:
        doomsday = total - (total // 7)*7
    else:
        doomsday = total

    return doomsday



def thirteen(year):
    keepTrack = {}
    for d in range(7):
        keepTrack[d] = 0
    for y in range(1900, year):
        for m in range(12):
            apart = 13 - doomsdate(y)[m]
            if apart < 0:
                if isLeap(y):
                    final = findDoomsday(y) - 2
                    if final < 0:
                        final = 6 + final
                else:
                    final = findDoomsday(y) - 1
                    if final < 0:
                        final = 6
                    print(f"the doomsday is {findDoomsday(y)}")
            else:
                final = findDoomsday(y) + (apart % 7)
            # print(f"month {m} year {y} and final {final}")
            while final > 6:
                final -= 7
            print(f"month is {m}")
            print(f"year is {y}")
            print(isLeap(y))
            print(f"apart is {apart}")
            print(f"final is {final}")
            keepTrack[final] += 1
        # if y == 1904:
            # if y == 1904
            #     print(doomsdate(y))
            #     print(findDoomsday(y))
            #     print()
            #     print(f"apart is {apart}")
            #     print(f"final is {final}")
    return keepTrack


year = int(input())
# print(thirteen(1900 + 1))
print(thirteen(1900 + year))




    #         difference = 13 - doomsdate(y)[m]
    #         if difference < 0:
    #             total = findDoomsday(y) - 1
    #         else:
    #             total = difference + findDoomsday(y)
    #             if total > 6:
    #                 while total > 6:
    #                     difference -= 7
    #                     total = difference + findDoomsday(y)
    #                     print(f"year {y} month {m} and total {total} difference {difference}")
    #         keepTrack[total] += 1
    # return keepTrack







