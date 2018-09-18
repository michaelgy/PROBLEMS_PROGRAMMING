from sys import stdin
from heapq import heappush, heappop

r = stdin.readline
INF = float('inf')

nodesm = 1000
adjl = [[] for i in range(nodesm)]
mndist = [INF]*nodesm
visit = [0]*nodesm
banks = []
poli = []


def dijkstra(s):
    mndist[s] = 0
    heap = [(0,s)]
    while heap:
        w,u = heappop(heap)
        for v,wi in adjl[u]:
            if mndist[v]>mndist[u]+wi:
                mndist[v] = mndist[u]+wi
                heappush(heap,(wi,v))
    return

def clean(nodes):
    for e in range(nodes):
        mndist[e] = INF
        adjl[e] = []

def brobbery(nodes):
    for e in poli:
        dijkstra(e)
    maxvalue = -1
    minimals = []
    for e in banks:
        if mndist[e]>maxvalue:
            maxvalue = mndist[e]
    for e in banks:
        if mndist[e] == maxvalue:
            minimals.append(e)
    print(len(minimals),maxvalue if maxvalue!=INF else "*")
    minimals.sort()
    for e in minimals[:len(minimals)-1]:
        print(e,end=" ")
    print(minimals[-1])

l = r().strip()
while l:
    N,M,B,P = map(int,l.split())
    clean(N)
    for e in range(M):
        a,b,w = map(int,r().split())
        adjl[a].append((b,w))
        adjl[b].append((a,w))
    banks = [int(i) for i in r().split()]
    poli = [int(i) for i in r().split()]
    brobbery(N)
    l = r().strip()
        
