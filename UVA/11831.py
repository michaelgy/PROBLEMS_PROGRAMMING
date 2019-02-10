from sys import stdin

r = stdin.readline
rally = [[""]*100 for i in range(100)]
out = []

def move(command,pos,m,n):
    result = 0
    if command == "D":
        pos[2] = (pos[2]+1)%4
    elif command == "E":
        pos[2] = (pos[2]-1)%4
    else:
        if pos[2] == 0 and pos[0]>0 and rally[pos[0]-1][pos[1]] != "#":
            pos[0]-=1
        elif pos[2] == 1 and pos[1]<n-1 and rally[pos[0]][pos[1]+1] != "#":
            pos[1]+=1
        elif pos[2] == 2 and pos[0]<m-1 and rally[pos[0]+1][pos[1]] != "#":
            pos[0]+=1
        elif pos[2] == 3 and pos[1]>0 and rally[pos[0]][pos[1]-1] != "#":
            pos[1]-=1
        if rally[pos[0]][pos[1]] == "*":
            rally[pos[0]][pos[1]] = "."
            result = 1
    return result

m,n,s = map(int,input().split())
while m:
    pos = []
    for e in range(m):
        line = input()
        for i in range(n):
            rally[e][i] = line[i]
            if line[i] not in ".*#":
                pos = [e,i,"NLSO".find(line[i])]
                
    count = 0
    for e in input().strip():
        count += move(e,pos,m,n)
    out.append("{}\n".format(count))
    m,n,s = map(int,input().split())
print("".join(out),end="")
