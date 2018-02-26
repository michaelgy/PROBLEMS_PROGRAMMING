import math
n = int(input())
while n:
    print("Printing order for {} pages:".format(n))
    if n == 1:
        print("Sheet 1, front: Blank, 1")
    else:
        sheets = math.ceil(n/4)
        pages = sheets*4
        fw,bw = 1,pages
        for e in range(sheets):
            for i in range(2):
                if i:
                    text = "back "
                    v1 = fw
                    v2 = bw if bw <= n else "Blank"
                else:
                    text = "front"
                    v1 = bw if bw <= n else "Blank"
                    v2 = fw
                fw +=1
                bw -=1
                print("Sheet {}, {}: {}, {}".format(e+1,text,v1,v2))
    n = int(input())
