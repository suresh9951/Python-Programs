def last_name(s):
    word=s.split()
    r=''
    for i in range(len(word)-1):
        r=r+word[i][0]+"."
    r=r+" "+word[-1]
    return r

s=input("enter name:") #abc xyz efgh
r=last_name(s)
print(r) # a.x. efgh
