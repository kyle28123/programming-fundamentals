#Kyle Bruce 000988034
#App to guess a random number

import random

secret_number = random.randint(1,100)

guess_count = 0

while True:
    guess_input = input("Guess a number between 1 and 100: ")

    if not guess_input.isdigit():
        print("Error: Please enter a valid whole number")
        continue

    guess = int(guess_input)

    if guess < 1 or guess >100:
        print("Error: Number must be between 1 and 100.")
        continue

    guess_count += 1

    if guess < secret_number:
        print("too low!")
    elif guess > secret_number:
        print("too high!!")
    else:
        print("YEAH! you guess it in " + str(guess_count) + " tries")
        break
    
