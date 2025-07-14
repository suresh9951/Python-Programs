def change_case(s):
    u=s.upper()
    l=s.lower()
    res=''
    for i in range(len(s)):
        if(s[i]==u[i]):
            res=res+l[i]
        elif(s[i]==l[i]):
            res=res+u[i]
    return res

s=input("enter a string:")
print(change_case(s))

"""p=swapcase (s)
print(s)"""


