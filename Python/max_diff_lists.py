def max_diff_lists(arr1,arr2):
    return max(abs(abs(max(arr1)-min(arr2))),abs(max(arr2)-min(arr1)))
n=int(input())#3
m=int(input()) #5
arr1=list(map(int,input().split()))[:n] #2 5 4
arr2=list(map(int,input().split()))[:m] #7 4 2 9 5
print(max_diff_lists(arr1,arr2)) #7
