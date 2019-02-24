from sys import stdin

lines = stdin.readlines()
out = []

def get_next():
    for e in lines:
        for j in map(int,e.split()):
            yield j

def get6_next(gnext):
    return next(gnext),next(gnext),next(gnext),next(gnext),next(gnext),next(gnext)
gnext = get_next()
maze = [[-1]*13 for i in range(13)]
mazemove = [[-1]*13 for i in range(13)]

r,c,sr,sc,tr,tc = get6_next(gnext)
moveseq = ((0,-1),(-1,0),(0,1),(1,0))

def next_move(r,c,sr,sc,srn,scn,mt):
    vm = False
    if 0<=srn and srn<r:
        if 0<=scn and scn<c:
            if mazemove[srn][scn]<0:
                q1 = mt == 0 and maze[srn][scn] != 1 and maze[srn][scn] != 3
                q2 = mt == 1 and maze[srn][scn] != 2 and maze[srn][scn] != 3
                q3 = mt == 2 and maze[sr][sc] != 1 and maze[sr][sc] != 3
                q4 = mt == 3 and maze[sr][sc] != 2 and maze[sr][sc] != 3
                vm = q1 or q2 or q3 or q4
    return vm
mazecount = 1
while r and c:
    sr,sc,tr,tc = sr-1,sc-1,tr-1,tc-1
    for j in range(r):
        for k in range(c):
            maze[j][k] = next(gnext)
            mazemove[j][k] = -1

    path = [[sr,sc,0]]
    mc = 1
    mazemove[sr][sc] = mc
    mc += 1
    while len(path)>0 and (path[-1][0] != tr or path[-1][1] != tc):
        if path[-1][2]<4:
            sra = path[-1][0]
            sca = path[-1][1]
            srn = sra+moveseq[path[-1][2]][0]
            scn = sca+moveseq[path[-1][2]][1]
            if next_move(r,c,sra,sca,srn,scn,path[-1][2]):
                mazemove[srn][scn] = mc
                mc += 1
                path.append([srn,scn,0])
            else:
                path[-1][2] += 1
        else:
            mazemove[path[-1][0]][path[-1][1]] = 0
            mc -= 1
            path.pop()
            if len(path)>0:
                path[-1][2] += 1
    out.append("Maze "+str(mazecount))
    out.append("")
    out.append('+'+'---+'*c)
    for j in range(r):
        mazer = ["|"]
        mazerl = []
        if j<r-1:
            mazerl.append("+")
        for k in range(c):
            cell = mazemove[j][k]
            mcell = "{:>3}".format(cell if cell > 0 else "???" if cell == 0 else "")
            if (maze[j][k] == 1 or maze[j][k] == 3) and k<c-1:
                mcell += "|"
            elif k<c-1:
                mcell += " "
            if j<r-1:
                mazerl.append("   +" if maze[j][k] != 2 and maze[j][k] != 3 else "---+")
            mazer.append(mcell)
        mazer.append("|")
        out.append("".join(mazer))
        if mazerl:
            out.append("".join(mazerl))
    out.append('+'+'---+'*c)
    out.append("")
    out.append("")
    mazecount += 1
    r,c,sr,sc,tr,tc = get6_next(gnext)
print("\n".join(out))
