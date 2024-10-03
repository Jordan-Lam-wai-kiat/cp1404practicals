import random

def main():
    """takes user input and prints result"""
    score = float(input("Enter score: "))
    grade = calculate_score(score)
    print(score, grade)
    random_score = random.randint(1, 100)
    grade = calculate_score(random_score)
    print(random_score, grade)

def calculate_score(score):
    """calculates the grade that should be given for the score"""
    if score < 0:
        "Invalid score"
    else:
        if score > 100 or score < 0:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        elif score < 50:
            return "Bad"

if __name__ == "__main__":
    main()