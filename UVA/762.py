from sys import stdin

r = stdin.readline
l = r().strip()

g = dict()

out = []

while l:
    g.clear()
    n = int(l)
    for i in range(n):
        u,v = r().split()
        if u in g:
            if v not in g[u][0]:
                g[u][0].add(v)
        else:
            g[u] = [set(),None,False]
            g[u][0].add(v)
        if v in g:
            if u not in g[v][0]:
                g[v][0].add(u)
        else:
            g[v] = [set(),None,False]
            g[v][0].add(u)
    s,t = r().split()
    nfnd = True
    i= 0 if (s in g) and (t in g) else 1
    nlist = [s]
    while nfnd and i<len(nlist):
        u = nlist[i]
        g[u][2] = True
        for v in g[u][0]:
            if v == t:
                nfnd = False
            if not g[v][2]:
                g[v][1] = u
                g[v][2] = True
                nlist.append(v)
        i+=1
    if nfnd:
        out.append("No route")
    else:
        route = []
        a = t
        while a != s:
            route.append("{} {}".format(g[a][1],a))
            a = g[a][1]
        route.reverse()
        out.extend(route)
    r()
    l = r().strip()
    if l:
        out.append("")
print("\n".join(out))
