def carry(n,m):
    carry=0
    count1=0
    c=0
    while(n>0 or m>0 or carry>0):
        r1=n%10
        r2=m%10
        c=r1+r2+carry
        if(c>9):
            carry=1
            count1=count1+1
        else:
            carry=0
        n=n//10
        m=m//10
        c=0
    return count1

n=int(input())
m=int(input())
print(carry(n,m))
