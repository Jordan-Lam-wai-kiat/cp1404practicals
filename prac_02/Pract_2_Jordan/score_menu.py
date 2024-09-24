from score import calculate_score
import random

def main(score):
    """Selection menu for User"""
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
    user_input = input("Please choose an option: ").upper()
    if user_input == "G":
        score = get_score()
    showing_output(user_input, score)

def get_score():
    """gets a random score and stores it as new score"""
    random_score = random.randint(1, 100)
    return random_score

def get_stars(score):
    """Returns number of stars equivalent of score"""
    stars = (score * "*")
    return stars

def input_score():
    """Asks for score in initial startup"""
    score = int(input("Please input a score: "))
    return score

def showing_output(user_input, score):
    """Decides which course of action to take based on user input and loops menu unless 'Q' is enetered"""
    if user_input == "G":
        score = get_score()
        return print(score), main(score), score
    elif user_input == "P":
        result = calculate_score(score)
        return print("Your score is", score, "Your grade is: ", result,"!"), main(score)
    elif user_input == "S":
        stars = get_stars(score)
        return print(stars), main(score)
    elif user_input == "Q":
        print("Thank you, Goodbye.")

    else:
        re_enter_choice = input("Please enter a valid option (G, P, S, Q): ").upper()
        return showing_output(re_enter_choice, score)

if __name__ == "__main__":
    score = input_score()
    main(score)
