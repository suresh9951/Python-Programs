def perfect_cubes(n):
    d=round(n**(1/3))
    if(d**3==n):
        return 1
    else:
        return 0
n=int(input())#10
l=list(map(int,input().split()))[:n] #2 3 4 1 6 8 27 64 45 76
c=0
for p in l:
    d=perfect_cubes(p)
    c=c+d
print(c)#4
