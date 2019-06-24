from sys import stdin

lines = stdin.readlines()

out = []

possible = ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']

def count_mov(label,b):
    total = 0
    if label == 'B':
        total = b[1]+b[2]
    elif label == 'G':
        total = b[0]+b[2]
    else:
        total = b[0]+b[1]
    return total

for line in lines:
    if line.strip():
        values = list(map(int,line.split()))
        b1,b2,b3 = values[:3],values[3:6],values[6:]
        label = ''
        mov = float("inf")
        for e in possible:
            total = count_mov(e[0],b1)+count_mov(e[1],b2)+count_mov(e[2],b3)
            if total<mov:
                label = e
                mov = total
        out.append("{} {}".format(label,mov))

print("\n".join(out))
    
