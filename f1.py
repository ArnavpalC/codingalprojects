file = open("student.txt", "w")
file.write("This is the original file content.\n")
file.close()

file = open("student.txt", "r")
print("Reading File:")
print(file.read())
file.close()

file = open("student.txt", "a")
file.write("This line was added using append mode.\n")
file.close()

file = open("student.txt", "r")
print("\nUpdated File Content:")
print(file.read())
file.close()
