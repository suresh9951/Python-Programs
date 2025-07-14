# inverted hallow pyramid
n=int(input("enter a number:"))
for i in range(1,n+1):
    if (i==1):
        print("* "*n)
    else:
        for j in range(1,(2*n)):
            if (i==j or i+j==2*n):
                print("*",end="")
            else:
                print(" ",end="")
        print()
                