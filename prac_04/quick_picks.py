import random


user_input = int(input("How many quick picks? "))

for count in range(1, user_input + 1, +1):
    CONSTANTS = []
    for num in range(1, 7):
        random_num = random.randint(1, 45)
        while random_num in CONSTANTS:
            random_num = random.randint(1, 45)
        else:
            CONSTANTS.append(random_num)
    CONSTANTS.sort()
    print(f"{CONSTANTS[0] : 3}{CONSTANTS[1] : 3}{CONSTANTS[2] : 3}{CONSTANTS[3] : 3}{CONSTANTS[4] : 3}{CONSTANTS[5] : 3}")
