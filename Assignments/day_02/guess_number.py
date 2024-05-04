## this is a game for users to guess a number between 1-20


import random

number = random.randrange(1, 21)
print("I am thinking of a number between 1 to 20")
guess_try = 0
while True:
    guess = int(input("What is your guess? :"))
    guess_try = guess_try + 1
    if guess == number:
        print(
            f"You are right, that is the number. Your number of tries was: {guess_try}"
        )
        break
    elif guess < number:
        print("The number is bigger ")
    else:
        print("The number is smaller")
