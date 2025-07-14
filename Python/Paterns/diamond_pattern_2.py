n = int(input("enter a number:"))
for i in range(1, n + 1):
    sb=n-i+1
    print(" "*(sb-1)+"* "*i)
for i in range(n-1,0,-1):
    sb=n-i+1
    print(" "*(sb-1)+"* "*i)
    