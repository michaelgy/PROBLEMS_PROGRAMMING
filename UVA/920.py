from math import sqrt

def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def proy_x(y0,x1,y1,x2,y2):
    return (y0-y2)*(x2-x1)/(y2-y1)+x2

t = int(input())
while t:
    p = int(input())
    x = []
    for i in range(p):
        x.append([int(j) for j in input().split()])
    x.sort(reverse=True,key= lambda y:y[0])
    ymax = x[0][1]
    imax = 0
    tdist = 0
    for i in range(1,p):
        if(x[i][1] > ymax):
            xp = proy_x(ymax,x[i-1][0],x[i-1][1],x[i][0],x[i][1])
            tdist += dist(xp,ymax,x[i][0],x[i][1])
            ymax = x[i][1]
            imax = i
    print("{:.2f}".format(tdist))
    t-=1
