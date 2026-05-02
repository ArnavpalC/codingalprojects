def is_power_of_8(n):
    if n <= 0:
        return False
    
    if (n & (n - 1)) != 0:
        return False
    
    count = 0
    temp = n
    
    while temp > 1:
        temp >>= 1
        count += 1
    
    return count % 3 == 0


num = int(input("Enter a number: "))

if is_power_of_8(num):
    print("Yes, it is a power of 8")
else:
    print("No, it is not a power of 8")
