a=int(input())
s=list(str(a))

i=len(s)-2
while (i>=0 and s[i]>=s[i+1]):
    i=i-1
if (i==-1):
    print("-1")
    
else:    
    j=len(s)-1
    while (s[i]>=s[j]):
        j=j-1

    s[i],s[j]=s[j],s[i]
    s=s[:i+1]+sorted(s[i+1:])
    next=int("".join(s))
    print(next)