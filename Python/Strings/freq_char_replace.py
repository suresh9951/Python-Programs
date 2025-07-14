def freq_char_replace(s,x):
    m=''
    c=0
    mc=0
    for i in s:
        c=s.count(i)
        if (c>=mc):
            mc=c
            r=i
    for i in s:
        if r==i:
            m=m+x
        else:
            m=m+i
    return m
s=input("enter a string:") #bbadbbababb
x=input("enter replacing character:") #t
v=freq_char_replace(s,x)
print(v) #ttadttatatt