print("=== exam Form ===")

name = input("Enter your name: ")

while True:
    age = int(input("Enter your age: "))
    if age >= 18:
        break
    else:
        print("You must be at least 18 years old to apply.")

email = input("Enter your email: ")

print("\n=== Application Details ===")
print("Name:", name)
print("Age:", age)
print("Email:", email)
