from sys import stdin
r = lambda : stdin.readline().strip()

gm = lambda start,stop,mult: [x*mult for x in range(start,stop)]
pvl = gm(1,21,1) + gm(1,21,2) + gm(1,21,3) + [0,50]
pvs = set(pvl)
pvl = list(pvs)
pos = dict()
for i,x in enumerate(pvl):
    for j,y in enumerate(pvl[i:]):
        for z in pvl[j+i:]:
            v = x+y+z
            d = len(set((x,y,z)))
            if d == 3:
                p = 6
            elif d == 2:
                p = 3
            else:
                p = 1
            if v in pos:
                pos[v][0] += 1
                pos[v][1] += p
            else:
                pos[v] = [1,p]
            
n = int(r())
while n>0:
    if n in pos:
        print("NUMBER OF COMBINATIONS THAT SCORES {} IS {}.".format(n,pos[n][0]))
        print("NUMBER OF PERMUTATIONS THAT SCORES {} IS {}.".format(n,pos[n][1]))
    else:
        print("THE SCORE OF {} CANNOT BE MADE WITH THREE DARTS.".format(n))
    print("*"*70)
    n = int(r())
print("END OF OUTPUT")
