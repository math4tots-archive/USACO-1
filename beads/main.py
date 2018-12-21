def sortBeads(beads):
    necklace = beads + beads
    cluster = []
    color = 'b'
    count = 0
    for bead in necklace:
        if bead == color or bead == 'w':
            count += 1
        else:
            cluster.append(count)
            color = bead
            count = 1
    print(cluster)
    return cluster

def mostBeads(beads):
    biggest = 0
    together = 0
    cluster = sortBeads(beads)
    for b in range(len(cluster)):
        print(together)
        if cluster[b] > biggest:
            biggest = cluster[b]
        if cluster[b] != cluster[len(cluster) - 1]:
            if cluster[b] + cluster[b + 1] > together:
                together = cluster[b] + cluster[b + 1]
    return together

input()
beads = input()
print(mostBeads(beads))



