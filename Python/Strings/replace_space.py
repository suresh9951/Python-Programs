def str_modify(s):
    r=''
    for i in range(len(s)):
        if(s[i]==chr(32)):
           r=r+'-'
        else:
            r=r+s[i]
    return r
s=input("enter string:")
print(s)
print(str_modify(s))


'''def split_and_join(line):
    line=line.split()
    line='-'.join(line)
    return line
print(split_and_join(input()))'''


           
