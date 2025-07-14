def palindrome(n):
    r=n
    sum1=0
    while(n>0):
        rem=n%10
        sum1=sum1*10+rem
        n=n//10
    if(r==sum1):
        return "palindrome"
    else:
        return "not palindrome"
n=int(input())
print(palindrome(n))

'''n=input()
if n==n[::-1]:
    print("pali")
else:
    print("not")'''
