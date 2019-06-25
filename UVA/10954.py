from sys import stdin
import heapq

lines = stdin.readlines()

n = int(lines[0].strip())
i = 1
out = []
while n:
    numbs = []
    for e in lines[i].split():
        heapq.heappush(numbs,int(e))
    total = 0
    while len(numbs)>1:
        acum = heapq.heappop(numbs)+heapq.heappop(numbs)
        total += acum
        heapq.heappush(numbs,acum)
    i+=1
    n = int(lines[i].strip())
    i+=1
    out.append(str(total))

print("\n".join(out))
