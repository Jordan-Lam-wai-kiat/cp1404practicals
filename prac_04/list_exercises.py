usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
numbers = []
access_granted = False
count = 0

while access_granted is False:
    username = input("Please enter your username: ")
    if username in usernames:
        print("Access granted")
        access_granted = True
    else:
        print("Access denied")

while count < 5:
    try:
        user_input = int(input("Please enter a number: "))
        numbers.append(user_input)
        count += 1
    except ValueError:
        print("Please enter a valid whole number")

largest_number = max(numbers)
smallest_number = min(numbers)
last_number = numbers[-1]
first_number = numbers[0]
total = sum(numbers)
average = total / len(numbers)

print(f"The first number is {first_number}")
print(f"The last time number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average : .1f}")