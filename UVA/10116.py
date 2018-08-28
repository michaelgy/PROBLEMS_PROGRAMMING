from sys import stdin
r = stdin.readline

M = 10
grid = [[0]*M for i in range(M)]
reco = [[0]*M for i in range(M)]
path = [[0,0] for i in range(M*M)]

"""
0 = south
1 = west
2 = north
3 = east
"""
def movement(f,c):
    v = grid[f][c]
    if v == 0:
        return (f+1,c)
    if v == 1:
        return (f,c-1)
    if v == 2:
        return (f-1,c)
    if v == 3:
        return (f,c+1)


def robot(F,C,i):
    steps = 0
    cycle = 0
    ac = (0,i-1)
    path[0][0], path[0][1] = ac
    nend = True
    while nend:
        if ac[1] == C or ac[0] == F or ac[1] == -1 or ac[0] == -1:
            nend = False
        elif reco[ac[0]][ac[1]] == 1:
            steps -= 1
            cycle += 1
            while ac[0] != path[steps][0] or ac[1] != path[steps][1]:
                steps -= 1
                cycle += 1
            nend = False
        else:
            reco[ac[0]][ac[1]] = 1
            path[steps][0], path[steps][1] = ac
            ac = movement(*ac)
            steps += 1
    return (steps,cycle)
            
F,C,init = map(int,r().split())
while F:
    for i in range(F):
        l = r().strip()
        for j in range(C):
            ch = l[j]
            reco[i][j] = 0
            if ch == "S":
                grid[i][j] = 0 
            elif ch == "W":
                grid[i][j] = 1
            elif ch == "N":
                grid[i][j] = 2
            else:
                grid[i][j] = 3
    steps,cycle = robot(F,C,init)
    if cycle:
        print("{} step(s) before a loop of {} step(s)".format(steps,cycle))
    else:
        print("{} step(s) to exit".format(steps))
    F,C,init = map(int,r().split())
        
