from sys import stdin
r = stdin.readline
t = int(r())
i = 0
while t:
    i+=1
    t-=1
    cards = [e for e in r().split()]
    pile = cards[:27]
    y = 0
    for e in range(3):
        c = pile.pop()[0]
        c = int(c) if c.isdigit() else 10
        y+=c
        q = 10-c
        if q:
            pile = pile[:-q]
    pile = pile+cards[27:]
    print("Case {}: {}".format(i,pile[y-1]))