binary = input("Enter a binary number: ")

decimal = 0
power = 0

for digit in reversed(binary):
    if digit == '1':
        decimal += (1 << power)
    elif digit != '0':
        print("Invalid binary number!")
        exit()
    power += 1

print("Decimal value:", decimal)
