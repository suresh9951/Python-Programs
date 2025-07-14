def leader_element(l,n):
    r=[]
    for i in range(n-1):
        for j in range(i+1,n):
            if (l[j]>l[i]):
                break
        else:
            r.append(l[i])
            print(r)
    r.append(l[-1])
    print(r)
    return sum(r)
n=int(input())
l=list(map(int,input().split()))
r=leader_element(l,n)
print(r)
