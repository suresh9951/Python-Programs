def linear (arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
    
arr=list(map(int,input("enter elements:").split()))
target=int(input("enter target element:"))
res=linear(arr,target)
if res==-1:
    print(f"{target} element is not found in the array")
else:
    print(f"{target} element is  found at position {res+1} in the array")