#letter -G
n=int(input("enter a number:"))
for i in range(1,n+1):
    if (i==1 or i==n):
        print(" "+"*"*(n-1))
    elif(i==(n//2)+1):
        print("*"+" "*(i-1)+"*"*(i-1))
    elif(i>(n//2)+1):
        print("*"+" "*(n-2)+"*")
    else:
        print("*")
    