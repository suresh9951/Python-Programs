def pivot_element(n,l):
    total_sum=sum(l)
    left_sum=0
    for i in range(len(l)):
        right_sum=total_sum - left_sum -l[i]
        if(left_sum==right_sum):
            return i
        left_sum=left_sum+l[i]
    return -1

n=int(input())
l=list(map(int,input().split()))
r=pivot_element(n,l)
print(r)


