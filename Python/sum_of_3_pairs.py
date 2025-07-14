def sum_of_3_pairs(n,arr,target):
    count=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(target==arr[i]+arr[j]+arr[k]):
                    count=count+1
    return count
n=int(input())#10
arr=list(map(int,input().split()))[:n] #4 2 8 5 3 6 1 9 7 0
target=int(input())#20
print(sum_of_3_pairs(n,arr,target))#4
