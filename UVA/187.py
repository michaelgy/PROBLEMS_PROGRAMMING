from sys import stdin

lines = stdin.readlines()
acc = dict()
out = []
sne = True
i=0
while sne:
    line = lines[i]
    i+=1
    num = line[:3]
    if num != "000":
        acc[num] = line[3:][:-1]
    else:
        sne = False
seq = ""
b = 0
lseq = []
while i<len(lines):
    line = lines[i]
    i+=1
    seqi = line[:3]

    num = line[3:6]
    invalue = int(line[6:].strip())
    if seqi == seq:
        lseq.append((num,invalue))
        b += invalue
    else:
        if b!=0:
            out.append("*** Transaction {} is out of balance ***".format(seq))
            for e in lseq:
                if e[1]>-99 and e[1]<0:
                    se = "-0"
                else:
                    se = str(abs(e[1])//100)
                    if e[1]<0:
                        se = "-"+se
                out.append("{} {:<30} {:>7}.{:0>2}".format(e[0],acc[e[0]],se,abs(e[1])%100))
            if b>-99 and b<0:
                sb = "0"
            elif b>0 and b<99:
                sb = "-0"
            else:
                sb = str(abs(b)//100*-1)
                if b<0:
                    sb = sb[1:]
            out.append("{} {:<30} {:>7}.{:0>2}".format(999,"Out of Balance",sb,abs(b)%100))
            out.append("")
        lseq = [(num,invalue)]
        b = invalue
        seq = seqi
print("\n".join(out))
