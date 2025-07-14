#letter -B
n=int(input("enter a number:"))
for i in range(1,n+1):
    if i==1 or i==n :
        print("*"*(n-1))
    elif(i==(n//2)+1):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
    