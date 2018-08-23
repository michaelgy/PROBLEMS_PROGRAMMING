from sys import stdin

inf = float('inf')

def objective(x,y,z):
    return z*z-(x*x+y*y)

D = [[0,0] for i in range(41)]
memo = dict()
def mec(i,N,ec,x=0,y=0):
    if (x,y) in memo:
        return memo[(x,y)]
    minimun = inf
    if i==N:
        return inf
    obj = objective(x,y,ec)
    if obj == 0:
        return 0
    elif obj < 0:
        return minimun
    else:
        minimun = min(minimun,mec(i,N,ec,x=x+D[i][0],y=y+D[i][1])+1,mec(i+1,N,ec,x=x,y=y))
    memo[(x,y)] = minimun
    return minimun
r = stdin.readline
l = r().strip()
n = int(l)
while n:
    l = r().strip()
    while not l:
        l = r().strip()
    memo = dict()
    N,ec = map(int,l.split())
    for i in range(N):
        l = r().strip()
        while not l:
            l = r().strip()
        D[i][0],D[i][1] = map(int,l.split())
    result = mec(0,N,ec)
    print(result if result != inf else "not possible")
    n-=1
    
