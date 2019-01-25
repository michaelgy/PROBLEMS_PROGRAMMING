from sys import stdin

def bsearch(m,x):
    if not m:
        return 0
    left = 0
    n = len(m)-1
    while n-left>1:
        k = (n+left)//2
        if x<m[k]:
            n = k
        else:
            left = k
    if n == 0:
        n=1
    return left if m[left]>x else n if len(m)>n and m[n]>x else n+1

numbers = stdin.readlines()
m = []
out = []
for e in numbers:
    x = int(e.strip())
    m.insert(bsearch(m,x),x)
    n = len(m)
    if n%2 == 0:
        out.append((m[n//2]+m[n//2-1])//2)
    else:
        out.append(m[n//2])
print("\n".join(map(str,out)))
