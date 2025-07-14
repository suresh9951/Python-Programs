num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)

sum_of_powers = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers = sum_of_powers + (digit ** num_digits)
    temp_num = temp_num // 10

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.") # 1^3 + 5^3 + 3^3 = 153
else:
    print(f"{num} is not an Armstrong number.")
