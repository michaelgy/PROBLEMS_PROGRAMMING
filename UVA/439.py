from sys import stdin

def get_input():
    for line in stdin.readlines():
        if line.strip():
            a,b = line.split()
            yield ord(a[0])-ord('a'),int(a[1])-1,ord(b[0])-ord('a'),int(b[1])-1


out = []
board = [[True]*8 for i in range(8)]
movek = ((2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1))

def valid_move(nri,nci):
    vm = False
    if 0<=nri and nri<8:
        if 0<=nci and nci<8:
            vm = board[nri][nci]
    return vm

for c,r,tc,tr in get_input():
    for i in range(8):
        for j in range(8):
            board[i][j] = True
    mc = 0
    if c != tc or r != tr:
        nf = True
        nxtm = [(r,c,mc)]
        i = 0
        while nf and i<len(nxtm):
            ri,ci,mci = nxtm[i]
            i+=1
            mci+=1
            j = 0
            while nf and j<8:
                nri,nci = ri+movek[j][0],ci+movek[j][1]
                if nri == tr and nci == tc:
                    nf = False
                    mc = mci
                elif valid_move(nri,nci):
                    nxtm.append((nri,nci,mci))
                    board[nri][nci] = False
                j+=1
    x = chr(ord('a')+c)+str(r+1)
    y = chr(ord('a')+tc)+str(tr+1)
    out.append("To get from {} to {} takes {} knight moves.".format(x,y,mc))
print("\n".join(out))
    
