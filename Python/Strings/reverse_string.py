def invert(s):
    r=''
    str=s.split()
    for p in range(len(str)-1,-1,-1):
        d=str[p][::-1]
        if(p!=len(str)-1):
            r=r+d+" "
        else:
            r=r+d+" "
    return r
s=input("enter string:") #the boy ran
r=invert(s)
print(r)# nar yob eht

'''s=input()
print(s[::-1])'''
