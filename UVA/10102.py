from sys import stdin
r = lambda : stdin.readline().strip()

line = r()
while line:
    m = int(line)
    ones = []
    threes = []
    for i in range(m):
        for j,c in enumerate(r()):
            if c == "3":
                threes.append((i,j))
            elif c == "1":
                ones.append((i,j))
    mdist = float("-inf")
    
    for ti,tj in ones:
        mindist = float("inf")
        for i,j in threes:
            d = abs(i-ti)+abs(j-tj)
            if mindist>d:
                mindist = d
        
        if mindist>mdist:
            mdist = mindist
    print(mdist)
    line = r()
