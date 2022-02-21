import random

def guess(x):
    low = 1
    high = x
    random_number = random.randint(low, high)
    guess = 0
    while random_number != guess:
        guess = int(input(f"Guess a number between {low} and {high}: "))
        if guess < random_number:
            print(f"Sorry, guess again. Too low.")
            low = guess
        elif guess > random_number:
            print(f"Sorry, guess again. Too high.")
            high = guess

    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")

guess(10)            