def max_index(l,n):
    r=[]
    for i in range(1,n-1):
        if(l[i-1]>l[i] and l[i+1]>l[i]):
            d=(i-1)*(i+1)
            r.append(d)
    if(len(r)==0):
        return -1
    else:
        return max(r)
n=int(input("enter the size:"))
l=list(map(int,input("enter numbers:").split()))[:n]
r=max_index(l,n)
print(r)
