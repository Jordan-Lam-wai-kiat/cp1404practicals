password = ""
while len(password) < 10:
    password = input("Hello, input your password (minimum 10 char): ")

for i in range(0, len(password)):
    i += 1

print(i * "*")