from sys import stdin
r = stdin.readline
pmax = 1001
inf = float('inf')
adj = [[0]*pmax for i in range(pmax)]
gion = [inf]*pmax
index = [0]*pmax
mark = [0]*pmax
nxt = [0]*pmax

def gio(p):
    gion[0] = 0
    c = 1
    k=0
    di = 0
    mark[di] = 1
    while k<p:
        for i in range(0,index[di]):
            v = adj[di][i]
            if not mark[v]:
                nxt[c] = v
                mark[v] = 1
                gion[v] = gion[di]+1
                c +=1
        k+=1
        di = nxt[k]

def clean(p):
    for i in range(p):
        gion[i] = inf
        mark[i] = 0
        index[i] = 0

t = int(r().strip())
while t:
    t-=1
    l = r().strip()
    while not l:
        l = r().strip()
    p,d = map(int,l.split())
    clean(p)
    for i in range(d):
        a,b = map(int,r().split())
        adj[a][index[a]] = b
        index[a] += 1
        adj[b][index[b]] = a
        index[b] += 1
    gio(p)
    for i in gion[1:p]:
        print(i)
    if t:
        print()
