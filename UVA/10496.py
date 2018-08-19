from sys import stdin
r = stdin.readline
MNODES = 11
inf = float('inf')
ptdist = [[0]*(MNODES) for i in range(MNODES)]
nodesl = [[0,0] for e in range(MNODES)]
def dist(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def mdist(pa,pi,nodes):
    lnodes = len(nodes)
    if lnodes < 1:
        return dist(pa,pi)
    d = inf
    ni = set(nodes)
    for e in nodes:
        ni.remove(e)
        d = min(d,mdist(e,pi,ni)+dist(e,pa))
        ni.add(e)
    return d
sol = [[inf]*MNODES for i in range(2**(MNODES))]
def mdist_b(pa,bmask,n):
    if sol[bmask][pa] < inf:
        return sol[bmask][pa]
    if bmask == (1<<n)-1:
        return ptdist[pa][0]
    dist = inf
    for i in range(n):
        k = (1<<i)
        if (bmask & k) == 0:
            dist = min(dist,ptdist[pa][i]+mdist_b(i,bmask|k,n))
    sol[bmask][pa] = dist
    return dist

def clear(n):
    for e in range(2**n):
        for i in range(n):
            sol[e][i] = inf

c = int(r().strip())
while c>0:
    c-=1
    tx,ty = map(int,r().split())
    nodesl[0][0],nodesl[0][1] = map(int,r().split())
    tmp = {(nodesl[0][0],nodesl[0][1])}
    n = int(r().strip())
    n+=1
    clear(n)
    e = 1
    while e<n:
        x,y = map(int,r().split())
        if (x,y) not in tmp:
            tmp.add((x,y))
            nodesl[e][0],nodesl[e][1] = x,y
            for i in range(e):
                ptdist[i][e] = ptdist[e][i] = dist(nodesl[e],nodesl[i])
            e+=1
        else:
            n-=1
    
    print("The shortest path has length",mdist_b(0,1,n))



