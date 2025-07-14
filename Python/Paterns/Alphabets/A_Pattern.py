#letter -A
n=int(input("enter a number:"))
for i in range(1,n+1):
    sb=n-i
    if i==1:
        print(" "*(n-1)+"*")
    elif(i==(n//2)+1):
        print(" "*sb+"* "*(i))
    else:
        print(" "*sb+"*"+" "*((2*i)-3)+"*")