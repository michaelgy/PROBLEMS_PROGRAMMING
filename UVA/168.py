from sys import stdin
lines = stdin.readlines()
out = []
def simulate(g,m,t,k):
    litc = []
    nforw = True
    ki = 0
    count=0
    while nforw:
        i=0
        c = g[m][0]
        nn = True
        while i < len(c) and nn:
            if c[i] in g and g[c[i]][1] and c[i] != t:
                ki += 1
                t = m
                if ki == k:
                    ki = 0
                    litc.append(t)
                    g[t][1] = False
                m = c[i]
                nn = False
                
            else:
                i+=1
        nforw = i < len(c)
        count+=1
    return litc,m

i = 0
g = dict()
while i<len(lines)-1:
    for e in range(ord('A'),ord('Z')+1):
        g[chr(e)] = ['',True]
    line = lines[i].split()
    m,t,k = line[1],line[2],int(line[3])
    for c in line[0][:-1].split(";"):
        csp = c.split(":")
        if len(csp)>1:
            ck,ek = csp
        else:
            ck,ek = csp[0],''
        g[ck] = [ek,True]
    r = simulate(g,m,t,k)
    if r[0]:
        r[0].append('')
    out.append(" ".join(r[0])+"/"+r[1])
    i+=1
print("\n".join(out))
