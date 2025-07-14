def binary (arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1 
        else:
            high=mid-1
    return -1
    
arr=list(map(int,input("enter elements:").split()))
target=int(input("enter target element:"))
res=binary(arr,target)
if res==-1:
    print(f"{target} element is not found in the array")
else:
    print(f"{target} element is  found at position {res+1} in the array")

# input data should be in sorted order