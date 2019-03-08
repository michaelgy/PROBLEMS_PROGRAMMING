from sys import stdin

lines = stdin.readlines()
def get_token():
    for line in lines:
        line = line.strip()
        if line:
            yield line
out = []
gtoken = get_token()
n = int(next(gtoken,""))
while n:
    em,ef,sm,sf = 0,0,0,0
    pieces = 0
    for k in next(gtoken).split():
        pieces+=1
        if k[0] == "M":
            sm += 1
        else:
            sf +=1
        if k[1] == "M":
            em += 1
        else:
            ef += 1
    n-=1
    if em == sf and sm == ef and pieces>1:
        out.append("LOOP")
    else:
        out.append("NO LOOP")
print("\n".join(out))
