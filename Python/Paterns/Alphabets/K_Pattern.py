#letter -K
n=int(input("enter a number:"))
for i in range(1,(n//2)+1):
    sb=n-(2*i)-1
    print("*"+" "*(sb)+"*")
print("*")
for i in range((n//2),0,-1):
    sb=n-(2*i)-1
    print("*"+" "*sb+"*")
    