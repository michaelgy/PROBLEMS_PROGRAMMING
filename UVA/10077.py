from sys import stdin

read = stdin.readline
a,b = map(int,read().split())
while a+b > 2:
    l = [0,1]
    m = [1,1]
    r = [1,0]
    out = ""
    end = False
    if a==l[0] and b==l[1]:
        out = "L"
        end = True
    elif a==r[0] and b==r[1]:
        out = "R"
        end = True
    while not end:
        #print(l,m,r,out)
        if a==m[0] and b==m[1]:
            out = out if out != "" else "I"
            end = True
        else:
            if a*m[1] < b*m[0]:
                r = m[:]
                m[0] = m[0]+l[0]
                m[1] = m[1]+l[1]
                out += "L"
            else:
                l = m[:]
                m[0] = m[0]+r[0]
                m[1] = m[1]+r[1]
                out += "R"
    print(out if out else "I")
    a,b = map(int,read().split())
