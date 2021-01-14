from sys import stdin

r = lambda : stdin.readline().strip()

t = int(r())
for i in range(t):
    r() #n
    a = list(map(int, r().split()))
    s = 0
    j = 1
    for k in a[j:]:
        for h in a[:j]:
            if h<=k:
                s+=1
        j+=1
    print(s)
