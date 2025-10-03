import random

secret = random.randint(1, 20)  # Random number between 1 and 20
guess = None

while guess != secret:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < secret:
        print("Too low, try again!")
    elif guess > secret:
        print("Too high, try again!")
    else:
        print("🎉 Correct! You guessed the number.")
