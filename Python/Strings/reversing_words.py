def change_each_word(s):
    r=''
    str=s.split()
    for p in range(len(str)-1,-1,-1):
        d=str[p]
        if(p!=0):
            r=r+d+" "
        else:
            r=r+d
    return r
s=input() #the boy ran
r=change_each_word(s)
print(r)# ran boy the
