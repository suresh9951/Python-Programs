def max_element(l):
    a=list(map(str,l))
    b=''.join(a)
    c=list(map(int,b))
    c.sort()
    c.reverse()
    e=list(map(str,c))
    f=''.join(e)
    return f
    

n=int(input())
l=list(map(int,input().split()))[:n]
print(max_element(l))
