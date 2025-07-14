def str_rev(s):
    res=''
    for i in s:
        res=i+res
    return res

s=input()
print(s)
print(str_rev(s))


"""with reverse function
return s[::-1]"""
