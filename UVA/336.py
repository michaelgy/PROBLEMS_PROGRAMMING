from sys import stdin

lines = stdin.readlines()
tokens = []
for e in lines:
    e = e.strip()
    if e:
        tokens.extend(map(int,e.split()))

n = tokens[0]
g= dict()
out = []
nlist = []

token_i = 1
case = 0
while n:
    g.clear()
    elements = tokens[token_i:token_i+2*n]
    token_i+=2*n
    token_j=token_i
    while tokens[token_j]+tokens[token_j+1] != 0:
        token_j+=2
        
    for i in range(0,2*n,2):
        k,j = elements[i],elements[i+1]
        if k not in g:
            g[k] = [set(),True]
        g[k][0].add(j)
        if j not in g:
            g[j] = [set(),True]
        g[j][0].add(k)
    for i in range(token_i,token_j,2):
        case += 1
        nlist.clear()
        s,ttl = tokens[i],tokens[i+1]
        if tokens[i] in g:
            for k in g:
                g[k][1] = True
            g[s][1] = False
            nlist.append((s,ttl))
        t = 0
        ind = 0
        while ind<len(nlist):
            t+=1
            u,k = nlist[ind]
            ind+=1
            if k:
                for j in g[u][0]:
                    if g[j][1]:
                        nlist.append((j,k-1))
                        g[j][1] = False
        out.append("Case {}: {} nodes not reachable from node {} with TTL = {}.".format(case,len(g)-t,s,ttl))
    token_i=token_j+3
    n = tokens[token_j+2]
print("\n".join(out))
