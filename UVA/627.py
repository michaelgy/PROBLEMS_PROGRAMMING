from sys import stdin
lines = stdin.readlines()
routers = [[] for i in range(400)]
rparent = [None]*400
out = []

def dfs_path(s,t,n):
    for i in range(n):
        rparent[i] = None
    nxt = [s]
    i = 0
    nf = t != s
    path = []
    rparent[s] = s
    while i<len(nxt) and nf:
        j = 0
        rl = routers[nxt[i]]
        while j<len(rl) and nf:
            if rparent[rl[j]] == None:                
                rparent[rl[j]] = nxt[i]
                nxt.append(rl[j])
            if t == rl[j]:
                nf = False
            else:
                j+=1
        i+=1
    if not nf:
        i = t
        while i != s:
            path.append(i)
            i = rparent[i]
        path.append(s)
    return path

i=0
line = lines[i].strip()
            
while line and i<len(lines):
    i+=1
    n = int(line)
    for j in range(n):
        k,rs = lines[i].split("-")
        rs = rs.strip()
        i+=1
        k = int(k)-1
        routers[k].clear()
        if rs:
            rs = rs.split(",")
            for e in rs:
                if e.isdecimal():
                    routers[k].append(int(e)-1)
    m = int(lines[i].strip())
    out.append("-----")
    for j in range(m):
        i+=1
        s,t = map(int,lines[i].split())
        path = dfs_path(s-1,t-1,n)
        if path:
            path.reverse()
            out.append(" ".join(map(lambda x: str(x+1),path)))
        else:
            out.append("connection impossible")
    i+=1
    if i<len(lines):
        line = lines[i].strip()
print("\n".join(out))
    
                    
