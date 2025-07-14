def is_prime(n):
    if n<=1:
        return 0
    for i in range (2,n):
        if (n%i==0):
            return 0
    return 1
    
def prime_numbers(n):
    l=[]
    num=2
    while len(l)<n:
        if is_prime(num):
            l.append(num)
        num=num+1
    return l
            
    
n=int(input("enter a number="))
res=prime_numbers(n)
print(res)