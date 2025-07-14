def even_odd(a,n):
    s=""
    for i in range(n):
        if (a[i]%2==0):
            s=s+"even"
        else:
            s=s+"odd"
    return s

n=int(input())
a=list(map(int,input().split()))
print(even_odd(a,n))