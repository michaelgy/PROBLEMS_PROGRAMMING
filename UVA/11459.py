from sys import stdin
r = stdin.readline
t = int(r().strip())
while t:
    t-=1
    l = [int(e) for e in r().split()]
    p,sl,drolls = l
    posi = [0 for e in range(p)]
    ladders = dict()
    for e in range(sl):
        start,end = [int(e) for e in r().strip().split()]
        ladders[start-1] = end-1
    win = False
    i = 0
    for e in range(drolls):
        dice = int(r().strip())
        if not win:
            try:
                posi[i] += dice
                if posi[i] in ladders:
                    posi[i] = ladders[posi[i]]
                if posi[i] >= 99:
                    win = True
                    posi[i] = 99
            except Exception:
                print(i,p)
        i=(i+1)%p
    for i in range(p):
        print("Position of player {} is {}.".format(i+1,posi[i]+1))
