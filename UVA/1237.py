from sys import stdin

r = lambda : stdin.readline().strip()

T = int(r())
while T:
    T-=1
    D = int(r())
    data = []
    for i in range(D):
        M,L,H = r().split()
        data.append((int(L),int(H),M))
    data.sort()
    sindex = [d[0] for d in data]
    Q = int(r())
    for i in range(Q):
        P = int(r())
        k = bisect(sindex,P)
        double = False
        inr = False
        m = ""
        while k and not double:
            k -= 1
            if data[k][1] >= P:
                if inr:
                    double = True
                else:
                    inr = True
                    m = data[k][2]
        if inr and not double:
            print(m)
        else:
            print("UNDETERMINED")
    if T:
        print()

        
