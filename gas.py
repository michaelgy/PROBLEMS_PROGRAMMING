import sys
r = sys.stdin.readline

Gmax = 10000
intv = [[0,0] for i in range(Gmax)]

def mc(L,G):
    low = 0
    b = 0
    c = 0
    i = 1
    nend = True 
    while nend:
        if i == G or low>=L:
            if low<L:
                if intv[b][0]<=low and intv[b][1]>=L:
                    c+=1
                else:
                    c = -1
            nend = False
        elif intv[i][0]>low:
            if low<intv[b][0]:
                c = -1
                nend = False
            else:
                c+=1
                low = intv[b][1]
                b = i
        else:
            if intv[b][1]<intv[i][1]:
                b = i
        i+=1
    return c
            


L,G = map(int,r().split())
while L:
    for i in range(G):
        x,radix = map(int,r().split())
        intv[i][0],intv[i][1] = x-radix,x+radix
    intv[:G] = sorted(intv[:G],key = lambda i: i[0])
    res = mc(L,G)
    print(G-mc(L,G) if res>=0 else -1)
    L,G = map(int,r().split())
    
