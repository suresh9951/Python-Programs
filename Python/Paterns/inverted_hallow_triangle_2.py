# inverted hallow pyramid
n=int(input("enter a number:"))
for i in range(1,n):
    if (i==1):
        print("* "*n)
    else:
        sb=i-1
        sa=2*(n-i)-1 
        print(sb*" "+"*"+sa*" "+"*")
print(" "*(n-1)+"*")