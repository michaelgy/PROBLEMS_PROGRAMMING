from sys import stdin
from heapq import heappush,heappop


inf = float('inf')
nmax = 1000
cmax = 101
conex = [0]*nmax
cost = [0]*nmax
adjl = [[] for i in range(nmax)]
d = [[0]*cmax for i in range(nmax)]
heap = []
rank = [0]*nmax
r = stdin.readline

def findr(x):
    px = conex[x]
    if px!=x:
        px = findr(px)
        conex[x] = px
    return px

def union(x,y):
    px,py = findr(x),findr(y)
    if px!= py:
        rx,ry = rank[px],rank[py]
        if rx>=ry:
            conex[py] = px
            if rx == ry:
                rank[px]+=1
        else:
            conex[px] = py

def dijkstra(s,e,c):
    heap.clear()
    heappush(heap,(0,0,s))
    d[s][0] = 0
    while heap:
        total,ac,u = heappop(heap)
        if u == e:
            return total
        if d[u][ac] >= total:
            if ac < c and total+cost[u] < d[u][ac+1]:
                d[u][ac+1] = total+cost[u]
                heappush(heap,(total+cost[u],ac+1,u))
            for v,w in adjl[u]:
                if ac>=w:
                    newc = ac-w
                    if total < d[v][newc]:
                        d[v][newc] = total
                        heappush(heap,(total,newc,v))
    return -1

def clean(n):
    for i in range(n):
        conex[i] = i
        adjl[i].clear()
        rank[i] = 0

l = r().strip()
while l:
    n,m = map(int,l.split())
    values = r().split()
    for e in range(n):
        cost[e] = int(values[e])
    clean(n)
    for e in range(m):
        u,v,w = map(int,r().split())
        union(u,v)
        adjl[u].append((v,w))
        adjl[v].append((u,w))
    q = int(r().strip())
    while q:
        q-=1
        c,s,e = map(int,r().split())
        if findr(s) == findr(e):
            for i in range(n):
                for j in range(c+1):
                    d[i][j] = inf
            total = dijkstra(s,e,c)
            print(total if total>-1 else "impossible")
        else:
            print("impossible")
    l = r().strip()
