from sys import stdin

r = lambda : stdin.readline().strip()

ps = []
n = 0
def reachable(actsum,i,tsum):
    global n
    if actsum == n:
        return True
    elif actsum+tsum < n:
        return False
    else:
        i = i + 1
        for j,k in enumerate(ps[i:]):
            tsum -= k
            if reachable(actsum+k,j+i,tsum):
                return True
        return False

t = int(r())
for _ in range(t):
    n = int(r())
    r()
    ps = list(map(int,r().split()))
    print("YES" if reachable(0,-1,sum(ps)) else "NO")
    
    
    
