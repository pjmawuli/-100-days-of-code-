# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print(art.logo)
print(f"Welcome to the number guessing game.")
print(f"I'm thinking of a number between 1 and 100")

response = input("Choose a difficulty. Type 'easy' or 'hard'. ")
if response == "easy":
    num_tries = 10
elif response == "hard":
    num_tries = 5

number = random.randint(1, 100)
print(f"Psst the number is {number}")

while num_tries > 0:
    print(f"You have {num_tries} remaining.")
    guess = int(input("Guess the number: "))

    if guess == number:
        print(f"You did it! the number was {number}")
        break
    elif guess > number:
        print(f"Your guess is too high")
    else:
        print(f"Your guess is too low")
    num_tries -= 1

