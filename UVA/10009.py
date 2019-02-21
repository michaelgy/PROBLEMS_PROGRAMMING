from sys import stdin

out = []
r = stdin.readline
n = int(r().strip())
cities = dict()

for k in range(n):
    r()
    cities.clear()
    c,q = map(int,r().split())
    for j in range(c):
        a,b = r().split()
        a = a[0]
        b = b[0]
        if a not in cities:
            cities[a] = set()
        cities[a].add(b)
    for j in range(q):
        a,b = r().split()
        a = a[0]
        b = b[0]
        ra,rb = "",""
        cc = 0
        nc = ["R"]
        i = 0
        while cc<2:
            ci = nc[i][-1]
            if ci == a:
                cc+=1
                ra = nc[i]
            if ci == b:
                cc+=1
                rb = nc[i]
            if cc < 2:
                if ci in cities:
                    for cj in cities[ci]:
                        nc.append(nc[i]+cj)
            i+=1
        i = 0
        while  i<len(ra) and i<len(rb) and ra[i] == rb[i] :
            i+=1
        out.append("".join([ra[j] for j in range(len(ra)-1,i-1,-1)])+rb[i-1:])
    if k<n-1:
        out.append("")
print("\n".join(out))
