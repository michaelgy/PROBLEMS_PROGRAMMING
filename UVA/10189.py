from sys import stdin
def count(f,n,m,x,y):
    c = 0
    if x>0:
        if f[y][x-1] == '*':
            c+=1
        if y<n-1:
            if f[y+1][x-1] == '*':
                c+=1
        if y>0:
            if f[y-1][x-1] == '*':
                c+=1
    if x<m-1:
        if f[y][x+1] == '*':
            c+=1
        if y<n-1:
            if f[y+1][x+1] == '*':
                c+=1
        if y>0:
            if f[y-1][x+1] == '*':
                c+=1
    if y>0:
        if f[y-1][x] == '*':
            c+=1
    if y<n-1:
        if f[y+1][x] == '*':
            c+=1
    return c
r = stdin.readline
n,m = [int(e) for e in r().strip().split()]
field = []
for e in range(100):
    x = []
    for i in range(100):
        x.append(0)
    field.append(x)
num = 1
while n>0:
    for e in range(n):
        l = r().strip()
        for i in range(m):
            field[e][i] = '*' if l[i] == '*' else 0
    print("Field #{}:".format(num))
    for e in range(n):
        for i in range(m):
            if field[e][i] != '*':
                field[e][i] = count(field,n,m,i,e)
            print(field[e][i],end="")
        print()
    num+=1
    l = r().strip().split()
    while len(l) != 2:
        l = r().strip().split()
    n,m = [int(e) for e in l]
    if n>0:
        print()
    
