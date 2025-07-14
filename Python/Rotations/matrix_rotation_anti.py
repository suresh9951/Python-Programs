def rotate_anti_clock(m):
    n=len(m)
    for rows in m:
        rows.reverse()
    for i in range(n):
        for j in range(i):
            m[i][j],m[j][i]=m[j][i],m[i][j]
    return m


r=int(input("enter no.of rows="))
m=[]
for i in range(r):
    row=list(map(int,input().split()))
    m.append(row)
res=rotate_anti_clock(m)
print("anti clockwise matrix is")
for i in range(len(res)):
    print(*res[i])