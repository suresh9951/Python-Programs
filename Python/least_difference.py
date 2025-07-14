def least_diff(l,arr,n):
    r=[]
    for i in range(l):
        d=abs(arr[i]-n)
        r.append(d)
        s=min(r)
    return abs(n-s)   
l=int(input()) #12
arr=list(map(int,input().split()))[:l] #1 2 12 13 15 17 26 30 38 45 64 72
n=int(input()) #27
r=least_diff(l,arr,n)
print(r) #26
