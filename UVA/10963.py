from sys import stdin
r = stdin.readline
N = int(r().strip())
r()
while N>0:
    W = int(r().strip())
    d = 0
    cc = True
    if(W>0):
        yn,ys = [int(i) for i in r().strip().split()]
        d = abs(yn-ys)
    W-=1
    while W>0:
        yn,ys = [int(i) for i in r().strip().split()]
        d1 = abs(yn-ys)
        if d!=d1:
            cc = False
        W-=1
    if cc:
        print("yes")
    else:
        print("no")
    r()
    N-=1
    if(N>0):
        print()
