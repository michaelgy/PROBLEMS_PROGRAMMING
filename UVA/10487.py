from bisect import bisect
n = int(input())
numcase = 1
while n>0:
    nums = set()
    for e in range(n):
        nums.add(int(input()))
    nums = list(nums)
    l = len(nums)
    suma = []
    s = 0
    for e in range(l):
        for i in range(e+1,l):
            suma.append(nums[e]+nums[i])
            s += 1
    suma.sort()
    q = int(input())
    print("Case {}:".format(numcase))
    for e in range(q):
        qi = int(input())
        p = bisect(suma,qi)
        print("Closest sum to {} is ".format(qi),end="")
        if p == s:
            p-=1
        if p>0 :
            if abs(suma[p]-qi)< abs(suma[p-1]-qi):
                print(str(suma[p])+".")
            else:
                print(str(suma[p-1])+".")
        else:
            print(str(suma[p])+".")
    n = int(input())
    numcase += 1