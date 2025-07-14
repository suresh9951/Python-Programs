def happy(n):
    s=str(n)
    sum1=0
    for i in range(len(s)):
        sum1=sum1+int(s[i])
    r=str(sum1)
    if(sum1==1):
        return "happy"
    elif(len(r)>1):
        return happy(sum1)
    else:
        return "unhappy"
n=int(input("enter a number:"))
print(happy(n))
