from sys import stdin

r = stdin.readline

out = []

t = int(r().strip())

directions = "NESW"

def execute(c,pos,maze):
    if c == 'R':
        pos[2] = (pos[2]+1)%4
    elif c == 'L':
        pos[2] = (pos[2]-1)%4
    elif c == 'F':
        if pos[2] == 0 and maze[pos[0]-1][pos[1]] == ' ':
            pos[0] -= 1
        elif pos[2] == 1 and maze[pos[0]][pos[1]+1] == ' ':
            pos[1] += 1
        elif pos[2] == 2 and maze[pos[0]+1][pos[1]] == ' ':
            pos[0] += 1
        elif pos[2] == 3 and maze[pos[0]][pos[1]-1] == ' ':
            pos[1] -= 1

while t:
    t-=1
    r()
    rows,cols = map(int,r().split())
    maze = [r().strip() for e in range(rows)]
    pos = [int(i)-1 for i in r().split()]
    pos.append(0)
    nq = True
    while nq:
        i = 0
        line = r().strip()
        while i<len(line) and nq:
            if line[i] != 'Q':
                execute(line[i],pos,maze)
            else:
                nq = False
            i+=1
    out.append("{} {} {}".format(pos[0]+1,pos[1]+1,directions[pos[2]]))
print("\n\n".join(out))
            
        
    
