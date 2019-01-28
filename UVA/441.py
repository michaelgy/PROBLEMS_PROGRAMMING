from sys import stdin

lines = stdin.readlines()
k = 1
ind = 0
out = []
while k>0:
    data = list(map(int,lines[ind].split()))
    k = data[0]
    ind+=1
    if k:
        if len(out):
            out.append("")
        for m in range(1,len(data)-5):
            for n in range(m+1,len(data)-4):
                for o in range(n+1,len(data)-3):
                    for p in range(o+1,len(data)-2):
                        for q in range(p+1,len(data)-1):
                            for r in range(q+1,len(data)):
                                out.append(" ".join(map(str,[data[m],data[n],data[o],data[p],data[q],data[r]])))
    
print("\n".join(out))
            
