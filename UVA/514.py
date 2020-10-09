from sys import stdin

r = stdin.readline

def permutable(nums):
    n = len(nums)
    s = []
    nn = 1
    stable = True
    i = 0
    while stable and i<n:
        if not s:
            s.append(nn)
            nn+=1
        if nums[i] == s[-1]:
            i+=1
            s.pop()
        elif nums[i] > s[-1]:
            s.append(nn)
            nn+=1
        else:
            stable = False
    return stable

n = int(r().strip())
while n:
    nums = [int(i) for i in r().strip().split()]
    if nums[0]:
        print( "Yes" if permutable(nums) else "No")
    else:
        n = int(r().strip())
        print()
    
            
