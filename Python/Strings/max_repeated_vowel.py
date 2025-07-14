def max_repeated_vowel(s):
    c=0
    mc=0
    for i in s:
        c=s.count(i)
        if (c>mc):
            mc=c
            r=i
    return r
s=input() #abeoicaido
v=max_repeated_vowel(s)
print(v) #a
