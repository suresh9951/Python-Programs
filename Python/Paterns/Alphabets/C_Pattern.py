#letter -C
n=int(input("enter a number:"))
for i in range(1,n+1):
    sb=n-i
    if (i==1 or i==n):
        print(" "+"*"*(n-1))
    else:
        print("*")
    