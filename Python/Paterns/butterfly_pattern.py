n = int(input("enter a number:"))
#upper part
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
#lower part
for i in range(n-1,0,-1):
    for j in range(i):
        print("*", end=" ")
    for j in range(2*(n-i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()