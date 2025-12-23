
number = int(input("Enter a number: "))
sop = 0
temp = number

digits = len(str(number))

while temp > 0:
    digit = temp % 10
    sop += digit ** digits
    temp //= 10

if sop == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
