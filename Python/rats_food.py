def rats_food(r,unit,n,arr):
    sum1=0
    need=r*unit
    c=0
    if(len(arr)==0):
        return -1
    if(sum(arr)<(r*unit)):
        return 0
    else:
        for i in arr:
            sum1=sum1+i
            c=c+1
            if (sum1>=need):
                break
    return c
            
r=int(input("enter no of rats:"))
unit=int(input("available units:"))
n=int(input("no of rooms:"))
arr=list(map(int,input().split()))[:n]
print(rats_food(r,unit,n,arr))
