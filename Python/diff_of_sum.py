def diff_of_sum(n,d):
    sum1=0
    for i in range(1,n+1):
        if(n%i!=0):
            sum1=sum1+i
        else:
            sum1=sum1-i
    return sum1

n=int(input())
d=int(input())
print(diff_of_sum(n,d))
