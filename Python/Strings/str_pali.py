def str_pali(s):
    r=s[::-1]
    if(s==r):
        return "pali"
    else:
        return "not"
n=input()
print(str_pali(n))
    
