from sys import stdin

def differ_by_one(w0,w1):
    equal = False
    if len(w0) == len(w1):
        d = 0
        i = 0
        while i<len(w0) and d<2:
            if w0[i] != w1[i]:
                d+=1
            i+=1
        equal = d<2
    return equal

def get_graph(wlist):
    g = dict()
    for i in range(len(wlist)):
        wi = wlist[i]
        if wi not in g:
            g[wi] = [set(),True]
        for j in range(i+1,len(wlist)):
            wj = wlist[j]
            if wj not in g:
                g[wj] = [set(),True]
            if differ_by_one(wi,wj):
                g[wi][0].add(wj)
                g[wj][0].add(wi)
    return g

def get_min_distance(g,wa,wb):
    for w in g:
        g[w][1] = True
    nw = [(wa,0)]
    d = -1
    i = 0
    g[wa][1] = False
    while d == -1 and i<len(nw):
        wk,dk = nw[i]
        if wk == wb:
            d = dk
        else:
            for w in g[wk][0]:
                if g[w][1]:
                    nw.append((w,dk+1))
                    g[w][1] = False
        i+=1
    return d

out = []
r = stdin.readline
n = int(r().strip())
r()
wlist = []
for e in range(n):
    wlist.clear()
    w = r().strip()
    while w != '*':
        wlist.append(w)
        w = r().strip()
    g = get_graph(wlist)
    w = r().strip()
    while w:
        wa,wb = w.split()
        out.append("{} {} {}".format(wa,wb,get_min_distance(g,wa,wb)))
        w = r().strip()
    if e<n-1:
        out.append("")
print("\n".join(out))
    
