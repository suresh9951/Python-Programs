def small_large_sum(l):
    l1=[]
    l2=[]
    for i in range(len(l)):
        if i%2==0:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l1.sort()
    l2.sort()
    a=len(l1)
    b=len(l2)
    res=l1[a-2]+l2[b-2]
    return res

n=int(input())
l=list(map(int,input().split()))[:n]
print(small_large_sum(l))
