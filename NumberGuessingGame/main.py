import random
from art import art
number = random.randint(1, 100)


print(art)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    lives = 10
    print("You have", lives, "attempts remaining to guess the number.")

else:
    lives = 5
    print("You have", lives, " attempts remaining to guess the number.")

guess = int(input("Make a guess: "))
while not guess == number:
    if guess > number:
        print("Too high.")
    if guess < number:
        print("Too low.")

    lives -= 1
    if lives > 0:
        print("You have",  lives, "attempts remaining to guess the number.")
        print("Guess again.")
        print("")
        guess = int(input("Make a guess: "))
    if lives == 0:
        print("You've run out of guesses, you lose.")
        exit()

print("You got it! The answer was " + str(number) + ".")
