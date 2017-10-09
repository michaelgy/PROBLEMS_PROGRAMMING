from sys import stdin
import math

eps = 1e-8

def calc_dx(y,d):
    return math.sqrt(d**2-y**2)

def calc_dis(x,y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

n,d = map(int,stdin.readline().strip().split())
cases = 1
while n != 0:
    p = list()
    for e in range(n):
        p.append([int(e) for e in stdin.readline().strip().split()])
    p.sort(key=lambda x: x[1])
    p.sort(key=lambda x: x[0])
    c = 1
    if p[0][1]<=d:
        dx = p[0][0]+calc_dx(p[0][1],d)
    else:
        c = -1
    i = 1
    while c>0 and i<n:
        if p[i][1]>d:
            c=-1
        elif calc_dis([dx,0],p[i])-d>eps:
            dx = p[i][0]+calc_dx(p[i][1],d)
            c+=1
        i+=1
    print("Case {}: {}".format(cases,c))
    cases+=1
    stdin.readline()
    n,d = map(int,stdin.readline().strip().split())