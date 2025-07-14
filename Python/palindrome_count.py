a=int(input("enter first number="))
b=int(input("enter second number="))
c=0
for i in range(a,b):
    if str(i)==str(i)[::-1]:
        c=c+1
print(c)