def weight_of_string(s):
    w=0
    for p in s:
        d=10**(ord(p)-ord('A'))
        w=w+d
    return w
s=input() #dccbaa
s=s.upper()
w=weight_of_string(s)
print(w) # 1212
