from sys import stdin
r = stdin.readline

def dist(a,b):
    if a == b:
        return 0
    a,b = (a,b) if a<b else (b,a)
    d1 = b-a
    d2 = 9-b+a+1
    return d1 if d1<d2 else d2

def distk(k1,k2):
    t = 0
    for i in range(4):
        t+= dist(k1[i],k2[i])
    return t


Nmax = 501
keys = [[0,0,0,0] for i in range(Nmax)]
parent = [-1]*Nmax
inf = float('inf')

def repre(i):
    i = parent[i]
    while i!=-1 and parent[i] != i:
        i = parent[i]
    return i

def kruskal(edges,nodes):
    t = inf
    for e in range(nodes):
        i = distk(keys[0],keys[e+1])
        if i<t:
            t = i
    edg = 0
    i = 0
    while edg != nodes-1 and i<len(edges):
        w,u,v = edges[i]
        rpu = repre(u)
        rpv = repre(v)
        if rpu == -1:
            if rpv != -1:
                parent[u] = rpv
            else:
                mn = u if u<v else v
                parent[u],parent[v] = mn,mn
            t+= w
            edg += 1
        elif rpv == -1:
            parent[v] = rpu
            edg += 1
            t+= w
        elif rpu != rpv:
            mn = rpu if rpu<rpv else rpv
            parent[rpu],parent[rpv] = mn,mn
            t+=w
            edg += 1
        i+=1
    return t

def clean(nodes):
    for i in range(nodes+1):
        parent[i] = -1

c = int(r().strip())
while c:
    c-=1
    data = r().split()
    nodes = int(data[0])
    clean(nodes)
    for e in range(nodes):
        for i in range(4):
            keys[e+1][i] = int(data[e+1][i])
    edges = list()
    for e in range(1,nodes+1):
        for i in range(1,e):
            edges.append((distk(keys[i],keys[e]),i,e))
    edges.sort(key=lambda x: x[0])
    print(kruskal(edges,nodes))
