file_name = "coding_info.txt"

content = """
Coding is basically the computer language used to develop apps, websites, and software.
Without it, we’d have none of the most popular technology we’ve come to rely on such as Facebook, our smartphones, the browser.
It all runs on code.

To put it very simply, the code is what tells your computer what to do.
To go a bit deeper, computers don’t understand words.
They only understand the concepts of on and off.

Binary code represents these on and off signals as the digits 1 and 0.
In order to make binary code manageable, computer programming languages were formed.
"""
with open(file_name, "w") as file:
    file.write(content)

print("Content written to file successfully.\n")

with open(file_name, "r") as file:
    data = file.read()

print("File Content:")
print(data)

char_count = len(data)

word_count = len(data.split())

line_count = len(data.strip().split("\n"))

print("File Statistics:")
print(f"Number of characters: {char_count}")
print(f"Number of words: {word_count}")
print(f"Number of lines: {line_count}")

with open(file_name, "a") as file:
    file.write("\nCoding helps create modern technology.")

print("\nAdditional text appended successfully.")

with open(file_name, "r") as file:
    updated_data = file.read()

print("\nUpdated File Content:")
print(updated_data)
