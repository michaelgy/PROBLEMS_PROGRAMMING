from sys import stdin
lines = stdin.readlines()

def get_token():
    for e in lines:
        e = e.strip()
        if e:
            yield e

gtoken = get_token()
out = []
l = next(gtoken)
k = 1
while l:
    n,m,c = map(int,l.split())
    if n and m and c:
        consume = 0
        fb = False
        maxc = 0
        ci = [0]*n
        st = [False]*n
        for i in range(n):
            ci[i] = int(next(gtoken))
        i = 0
        while i<m:
            j = int(next(gtoken))-1
            if st[j]:
                consume -= ci[j]
                st[j] = False
            else:
                consume += ci[j]
                st[j] = True
            if consume > maxc:
                maxc = consume
            if consume > c:
                fb = True
            i+=1
        out.append("Sequence "+str(k))
        if not fb:
            out.append("Fuse was not blown.")
            out.append("Maximal power consumption was "+str(maxc)+" amperes.")
        else:
            out.append("Fuse was blown.")
        out.append("")
        k+=1
    l = next(gtoken,"")
print("\n".join(out))
