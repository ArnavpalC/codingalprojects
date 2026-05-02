def reverse_bits(n):
    binary = bin(n)[2:]
    reversed_binary = binary[::-1]
    return int(reversed_binary, 2)


num = int(input("Enter a number: "))

result = reverse_bits(num)

print("Reversed bit number:", result)
