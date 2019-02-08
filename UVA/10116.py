from sys import stdin

r = stdin.readline
rows,columns,n = map(int,r().split())
movec = [[0]*10 for i in range(10)]
out = []

def clean_movec(rows,columns):
    for i in range(rows):
        for j in range(columns):
            movec[i][j] = 0

def in_matrix(pos,rows,columns):
    return -1<pos[0] and pos[0]<rows and -1<pos[1] and pos[1]<columns

def move(pos,inst):
    if inst[pos[0]][pos[1]] == "W":
        pos[1] -= 1
    elif inst[pos[0]][pos[1]] == "E":
        pos[1] += 1
    elif inst[pos[0]][pos[1]] == "S":
        pos[0] += 1
    elif inst[pos[0]][pos[1]] == "N":
        pos[0] -= 1

while rows:
    inst = [r().strip() for e in range(rows)]
    pos = [0,n-1]
    n = 1
    clean_movec(rows,columns)
    while in_matrix(pos,rows,columns) and movec[pos[0]][pos[1]] == 0:
        movec[pos[0]][pos[1]] = n
        move(pos,inst)
        n+=1
    if in_matrix(pos,rows,columns):
        h = movec[pos[0]][pos[1]]
        out.append("{} step(s) before a loop of {} step(s)\n".format(h-1,n-h))
    else:
        out.append("{} step(s) to exit\n".format(n-1))
    rows,columns,n = map(int,r().split())

print("".join(out),end="")

