from sys import stdin

lines = stdin.readlines()

def get_token():
    for line in lines:
        line = line.strip()
        if line:
            yield line

gtoken = get_token()

out = []
l = next(gtoken,"")

case = 1
while l:
    n = int(next(gtoken,""))
    lenl = len(l)
    data = [0]*lenl
    acum = 0
    prev = l[0]
    for e in range(1,lenl):
        le = l[e]
        if l[e] != prev:
            acum+=1
        prev = le
        data[e] = acum
    out.append("Case "+str(case)+":")
    case+=1
    for e in range(n):
        i,j = map(int,next(gtoken).split())
        if data[i] == data[j]:
            out.append("Yes")
        else:
            out.append("No")
    l = next(gtoken,"")
print("\n".join(out))
