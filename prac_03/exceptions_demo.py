"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? Ans: When any other value asides from an "int" value is entered
2. When will a ZeroDivisionError occur? Ans: When the denominator input is a 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Ans: Yes, i've implemented a function to check if the denominator is a 0 and requests for user input again.
"""
def check_zero_error(denominator):
    """checks if the denominator is 0 and asks for user input again if it is"""
    print('Please enter a number asides from 0')
    denominator = int(input("Enter the denominator: "))
    return denominator

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    """checks if denominator is 0"""
    if denominator == 0:
        """calls functions to check denominator"""
        denominator = check_zero_error(denominator)
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")