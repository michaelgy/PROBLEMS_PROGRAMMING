from sys import stdin

lines = stdin.readlines()
out = []
E = int(lines[0])
g = dict()
for i in range(1,E+1):
    g[i-1] = [list(map(int,lines[i].split()[1:])),True]
for i in lines[E+2:]:
    i = int(i)
    bd,bt = 0,0
    d,t = 1,0
    for j in g:
        g[j][1] = True
    nlist = [(i,1)]
    g[i][1] = False
    j = 0
    while j<len(nlist):
        u,di = nlist[j]
        ti = 0
        for v in g[u][0]:
            if g[v][1]:
                g[v][1] = False
                ti+=1
                nlist.append((v,di+1))
        if di == d:
            t+=ti
        else:
            if t>bt:
                bt = t
                bd = d
            d+=1
            t=ti
        j+=1
    if t>bt:
        bt = t
        bd = d
    out.append("{} {}".format(bt,bd) if bd else "0")
print("\n".join(out))
