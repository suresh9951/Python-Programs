def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (1):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
res=compute_lcm(num1, num2)
print(f"lcm of {num1},{num2} is {res}")
