from sys import stdin
r = stdin.readline
l = r().strip()
B,N = [int(i) for i in l.split()]
while B != 0 and N!=0:
    O = [0 for i in range(B)]
    D = [0 for i in range(B)]
    l = r().strip().split()
    for e in range(B):
        D[e] = int(l[e])
    for e in range(N):
        d,c,m = [int(i) for i in r().split()]
        O[d-1] += m
        D[c-1] += m
    p = True
    for e in range(B):        
        if D[e] < O[e]:
            print("N")
            p = False
            break
    if p:
        print("S")
    l = r().strip()
    B,N = [int(i) for i in l.split()]
