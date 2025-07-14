def fun(s1,s2):
    s=""
    for i in s1:
        if i not in s2:
            s=s+i
    if s=="":
        return "empty"
    else:
        return s
s1=input()
s2=input()
print(fun(s1,s2))
            