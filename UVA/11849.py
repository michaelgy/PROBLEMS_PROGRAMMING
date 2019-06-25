from sys import stdin

lines = stdin.readlines()

out = []

n,m = map(int,lines[0].split())
i = 1

while n>0 or m>0:
    jack = set()
    jilly = set()
    for e in range(n):
        jack.add(lines[i].strip())
        i+=1
    for e in range(m):
        jilly.add(lines[i].strip())
        i+=1
    out.append(str(len(jack.intersection(jilly))))
    n,m = map(int,lines[i].split())
    i+=1
print("\n".join(out))
