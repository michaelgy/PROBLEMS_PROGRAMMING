import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
def bins(data,value):
    right = len(data)
    left = 0
    while right-left>1:
        mid = (right+left)//2
        if data[mid]<value:
            left = mid
        elif data[mid] == value:
            while mid>0 and data[mid]==value:
                mid-=1
            left = mid
            right = mid+1
        else:
            right = mid
    return left if data[left] == value else right if right<len(data) and data[right] == value else left

n = input()
w = 1
while n:
    data = list(map(int,input().split()))
    data.sort()
    
    w+=1
    m = int(input())
    try:
        input()
        n = input()
    except StopIteration:
        n = ""
    i = bins(data,m/2)
    sdata = data[i+1:]
    #print(data,sdata)
    a,b = 0,0
    while data[a]+sdata[b]!=m and i>-1:
        a = i
        b = bins(sdata,m-data[a])
        i-=1
    print("Peter should buy books whose prices are {} and {}.\n".format(data[a],sdata[b]))
    
    
