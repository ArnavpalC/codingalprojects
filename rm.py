def check_rightmost_bit(n):
    if n & 1:
        print("Rightmost bit is 1 (odd number)")
    else:
        print("Rightmost bit is 0 (even number)")


num = int(input("Enter a number: "))
check_rightmost_bit(num)
