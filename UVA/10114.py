l = input().split()
m,dp,loan,r = [float(e) for e in l]
while m>=0:
    rl = []
    for e in range(int(r)):
        vls =[float(i) for i in input().split()]
        vls[1] = 1-vls[1]
        rl.append(vls)
    dep = rl[0][1]
    cv = (loan+dp)*dep #car worth in month 0
    months = 0
    payment = loan/m
    i = 1
    while(loan-cv>=1e-8 and months<=m):
        months+=1
        if(i<r):
            if(rl[i][0]==months):
                dep = rl[i][1]
                i+=1
        loan-=payment
        cv *=dep
    print(months, "month" if months == 1 else "months")
    m,dp,loan,r = [float(e) for e in input().split()]