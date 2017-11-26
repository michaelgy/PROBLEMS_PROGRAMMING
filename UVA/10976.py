from sys import stdin

encontrar = lambda k,y: (y*k)/(y-k)

r = stdin.readline
l = r().strip()
while l:
    k = int(l)
    sol = []
    c = 0
    for y in range(k+1,k*2+1):
        x = encontrar(k,y)
        if x%1 == 0:
            sol.append([int(x),y])
            c+=1
    print(c)
    for e in sol:
        print("1/{} = 1/{} + 1/{}".format(k,e[0],e[1]))
    l = r().strip()
