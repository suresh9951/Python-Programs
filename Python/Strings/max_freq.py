def max_ferq(s):
    r=''
    max_count=0
    count=0
    max_char=''
    for i in s:
        count=s.count(i)
        if(count>max_count):
            max_count=count
            max_char=i
    return max_char
s=input("enter a string:")
r=max_ferq(s)
print(r)
        
