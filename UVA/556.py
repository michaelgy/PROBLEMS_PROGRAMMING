def minside(b,w,nmove):
    return 0<= nmove[0] and 0<= nmove[1] and nmove[0] < b and nmove[1] < w

def movement_map(dire):
    x = [[0,-1],[1,0],[0,1],[-1,0]]
    y = [3,0,1,2]
    return [x[dire:]+x[:dire],y[dire:]+y[:dire]]

def nmove(matrix,b,w,actual):
    f,c,dire = actual
    mmap,dmap = movement_map(dire)
    for e in range(4):
        if minside(b,w,[f+mmap[e][0],c+mmap[e][1]]):
            if matrix[f+mmap[e][0]][c+mmap[e][1]] != 1:
                return [f+mmap[e][0],c+mmap[e][1],dmap[e]]
    return None

def ver_matrix(matrix):
    for e in matrix:
        print("".join([str(i) for i in e]))

b,w = [int(e) for e in input().split()]
while b and w:
    matrix = []
    for e in range(b):
        matrix.append([int(i) for i in input()])
    #f,c, [0-3]. 0 down, 1 right, 2 up, 3 left
    actual = [b-1,0,1]
    while matrix[b-1][0] != 3:
        nextmove = nmove(matrix,b,w,actual)
        if matrix[actual[0]][actual[1]] == 0:
            matrix[actual[0]][actual[1]] = 2
        else:
            matrix[actual[0]][actual[1]]+=1
        actual = nextmove
    matrix[b-1][0] = 2
    conteo = [0 for e in range(5)]
    for e in matrix:
        for i in e:
            if i != 1:
                if i != 0 and i<6:
                    conteo[i-1] += 1
                elif i == 0:
                    conteo[i] += 1
    [print("{:>3}".format(e),end = "") for e in conteo]
    print()
    b,w = [int(e) for e in input().split()]
