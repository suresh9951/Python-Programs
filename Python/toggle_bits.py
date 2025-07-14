'''n=int(input("enter a number="))
b=bin(n)
print(b)
s=''
for i in b:
    if i=="0":
        s=s+"1"
    else:
        s=s+"0"
sum1=0
power=0
r=reversed(s)
for i in r:
    sum1=sum1+int(i)*(2**power)
    power=power+1
print(sum1)'''

n=int(input("enter a number="))
b=bin(n)[2:]
s=''
for i in b:
    if i=="0":
        s=s+"1"
    else:
        s=s+"0"
print(int(s,2))
