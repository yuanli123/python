def bSearch(data,x):
    if len(data)==0:
        return -1
    left=0
    right=len(data)-1
    while left<right:
        mid=(left+right)//2
        if data[mid]>x:
            right=mid-1
        elif data[mid]<x:
            left=mid+1
        else:
            return mid
    return -1
