from sys import stdin

def get_next():
    for line in stdin.readlines():
        line = line.strip()
        if line:
            yield line

def fit_figtab(figtab,N,M):
    tmp = []
    minc,minr,maxc,maxr = 100,100,-1,-1
    for e in range(N):
        line = next(getn)
        for f in range(M):
            if line[f] == '*':
                minc = minc if f>minc else f
                minr = minr if e>minr else e
                maxc = maxc if f<maxc else f
                maxr = maxr if e<maxr else e
        tmp.append(line)
    for line in tmp[minr:maxr+1]:
        figtab.append(line[minc:maxc+1])

def verify_fit(tab,fig):
    if len(tab) == 0:
        if len(fig) == 0:
            return False
        else:
            return True
    elif len(fig) == 0:
        return False
    elif len(tab)<len(fig) or len(tab[0])<len(fig[0]):
        return True
    i = 0
    nf = True
    while i < (len(tab)-len(fig)+1) and nf:
        j = 0
        while j < (len(tab[0])-len(fig[0])+1) and nf:
            k = 0
            nmiss = True
            while k < len(fig) and nmiss:
                l = 0
                while l < len(fig[0]) and nmiss:
                    if tab[i+k][j+l] == '.' and fig[k][l] == '*':
                        nmiss = False
                    l+=1
                k+=1
            if nmiss:
                nf = False
            j+=1
        i+=1
    return nf

out = []
            
getn = get_next()
n = int(next(getn))
for i in range(n):
    N,M,S = map(int,next(getn).split())
    table = []
    fit_figtab(table,N,M)
    figure = []
    for j in range(S):
        figure.clear()
        n,m = map(int,next(getn).split())
        fit_figtab(figure,n,m)
        out.append("No" if verify_fit(table,figure) else "Yes")
    out.append("")
print("\n".join(out))
        
