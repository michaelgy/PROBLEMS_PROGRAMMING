from math import ceil
T = int(input())
i = 0
while T>i:
    i+=1
    print("Case {}:".format(i),end=" ")
    k = int(input())
    tm = 0
    tj = 0
    for e in input().split():
        e = int(e)
        tm += ceil((e+1)/30)*10
        tj += ceil((e+1)/60)*15
    if(tm > tj):
        print("Juice {}".format(tj))
    elif(tm<tj):
        print("Mile {}".format(tm))
    else:
        print("Mile Juice {}".format(tm))
