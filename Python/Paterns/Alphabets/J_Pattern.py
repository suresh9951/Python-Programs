#letter -J
n=int(input("enter a number:"))
for i in range(1,n+1):
    if(i==1):
        print("*"*n)
    elif(i==n):
        print("*"*(n//2))
    else:
        print(" "*(n//2)+"*")
    