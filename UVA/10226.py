from sys import stdin
r = stdin.readline
t = int(input())
input()
while t>0:
    forest = dict()
    l = r().strip()
    while l:
        if l in forest:
            forest[l] += 1
        else:
            forest[l] = 1
        l = r().strip()
    names = [e for e in forest.keys()]
    names.sort()
    n = sum(forest.values())
    for e in names:
        print("{} {:.4f}".format(e,forest[e]/n*100))
    t-=1
    if t>0:
        print()

