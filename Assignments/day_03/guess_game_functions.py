## this is a game for users to guess a number between 1-20

import random

def think_number():
    return random.randrange(1, 21)

def get_guess():
    return input("What is your guess? (Enter 'x' to exit, 'n' to leave the current game, 's' to show the hidden number): ")

def check_guess(guess, number):
    if guess == "x": 
        return "exit"
    elif guess == "n": 
        return "leave"
    elif guess == "s": 
        print(f"The number I thought about is: {number}")
        return "leave"
    else:
        return int(guess)

def play_game():
    while True:
        number = think_number()
        print("I am thinking of a number between 1 to 20")
        guess_try = 0
        while True:
            guess = get_guess()
            result = check_guess(guess, number)
            if result == "exit":
                return False
            elif result == "leave":
                break
            elif result == "continue":
                continue
            else:
                guess_try += 1
                if result == number:
                    print(f"You are right, that is the number. Your number of tries was: {guess_try}")
                    break
                elif result < number:
                    print("The number is bigger ")
                else:
                    print("The number is smaller")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
        if play_again == "x": 
            break

play_game()
