def avg_ascii(s):
    sum1=0
    for i in range(len(s)):
        sum1=sum1+ord(s[i])
    return sum1/len(s)
s=input("enter a string:") #strong
r=avg_ascii(s)
print("%.2f"%r) #105.40
