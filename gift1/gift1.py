"""
ID: jennife29
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

def readline():
  return fin.readline().strip()

def gift(given, giver, money, receivers):
    if len(receivers) != 0:
        gift = int(money / len(receivers))
        for r in receivers:
            given[r] += gift
        given[giver] += (money % len(receivers) - money)

    return given



number = int(readline())
everyone = []
for n in range(number):
    everyone.append(readline())

given = {x:0 for x in everyone}

for person in range(number):
    giver = readline()
    money, ppl = [int(x) for x in readline().split()]
    receivers = []
    for r in range(ppl):
        receivers.append(readline())
    gift(given, giver, money, receivers)

for person in given:
    fout.write(f"{person} {given[person]}\n")
    # fout.write(f"{given[person]}")



fout.close()


#readline() = fin.readline()
#input().split() = fin.readline().split()
#print() = fout.write("\n")