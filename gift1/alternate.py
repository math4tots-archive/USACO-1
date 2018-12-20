"""
ID: jennife29
LANG: PYTHON3
TASK: gift1
"""
# fin = open ('gift1.in', 'r')
# fout = open ('gift1.out', 'w')


def gift(given, giver, money, receivers):
    if len(receivers) != 0:
        gift = int(money / len(receivers))
        for r in receivers:
            given[r] += gift
        given[giver] += (money % len(receivers) - money)

    return given



number = int(input())
everyone = []
for n in range(number):
    everyone.append(input())

given = {x:0 for x in everyone}

for person in range(number):
    giver = input()
    money, ppl = [int(x) for x in input().split()]
    receivers = []
    for r in range(ppl):
        receivers.append(input())
    gift(given, giver, money, receivers)

for person in given:
    print(f"{person} {given[person]}")










#
# fout.close()


#input() = input(
#input().split() = fin.readline().split()
#print() = fout.write("\n")