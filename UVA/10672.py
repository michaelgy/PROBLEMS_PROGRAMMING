from sys import stdin

r = stdin.readline

nmax = 10000
q = [0]*nmax
parent = [-1]*nmax
reco = [0]*nmax
childs = [0]*nmax
adj = dict()

def mt(n):
    root = 0
    while parent[root] != -1:
        root+=1
    i = 0
    reco[0] = root
    total = 1
    while i<n:
        for j in range(childs[reco[i]]):
            reco[total] = adj[reco[i]][j]
            total+=1
        i+=1
    i = n-1
    moves = 0
    while i>0:
        if parent[reco[i]]>-1:
            if q[reco[i]] == 0:
                q[parent[reco[i]]] -= 1
                moves += 1
                q[reco[i]] = 1
            elif q[reco[i]] > 1:
                q[parent[reco[i]]] += q[reco[i]]-1
                moves += q[reco[i]]-1
                q[reco[i]] -= q[reco[i]]-1
            elif q[reco[i]] <0:
                q[parent[reco[i]]] += q[reco[i]]-1
                moves += -q[reco[i]]+1
                q[reco[i]] += -q[reco[i]]+1
            
        i-=1
    return moves

def clear(n):
    for i in range(n):
        parent[i] = -1
        adj = dict()

n = int(r().strip())
while n:
    clear(n)
    for j in range(n):
        l = [int(i) for i in r().split()]
        v,nm,d = l[0]-1,l[1],l[2]
        q[v] = nm
        childs[v] = d
        for i in range(d):
            parent[l[3+i]-1] = v
        adj[v] = [i-1 for i in l[3:]]
    print(mt(n))
    n = int(r().strip())
