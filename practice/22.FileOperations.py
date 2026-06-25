# file = open("demo.txt", "r")
# content = file.read();
# print(content)
# file.close()

# with open("demo.txt", "r") as file:
#     content = file.read()
#     print(content)

# file = open("demo.txt")
# try:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# with open("demo.txt", "a") as file:
#     file.write("\nHello Python!")

# with open("demo.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("demo.txt", "wb") as file:
#     file.write(01000001)

# with open("demo.txt", "rb") as file:
#     data = file.read()
#     print(data)
    
# with open("demo.txt") as file:
#     content = file.read()
# print(content)

# with open("demo.txt") as file:
#     for line in file:
#         print(line)

# Write Single Line 
# with open("demo.txt", "w") as file:
#     file.write("Hello World!")

# Write Multiple Line
# with open("demo.txt", "w") as file:
#     file.write("Line 1\n")
#     file.write("Line 2\n")

# lines = [
#     "Apple\n",
#     "Banana\n",
#     "Orange\n"
# ]

# with open("fruits.txt", "w") as file:
#     file.writelines(lines)

# with open("fruits.txt", "a") as file:
#     file.write("Graphes\n")

# Working with CSV
# Reading CSV
import csv
# with open("demo.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#         for col in row:
#             print(col)

# Using DictReader
# with open("demo.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["industry_code_ANZSIC"], ":", row["industry_name_ANZSIC"])

# Writing CSV
# with open("demo.csv", "w", newline="") as file:
#     writer = csv.DictWriter(
#         file,
#         fieldnames=["industry_code_ANZSIC", "industry_name_ANZSIC"]
#     )
#     writer.writeheader()
#     writer.writerow({
#         "industry_code_ANZSIC": "R",
#         "industry_name_ANZSIC": "Arts and Recreation Services"
#     })

# Working with JSON
import json
# user = {
#     "name": "Nil",
#     "age": "26"
# }
# with open("users.json", "w") as file:
#     json.dump(user, file)

# with open("users.json", "w") as file:
#     json.dump(user, file, indent=4)

# with open("users.json") as file:
#     data = json.load(file)
#     print(data)

user = '{"name": "Nil", "age": "26"}'
data = json.loads(user)
print(data)