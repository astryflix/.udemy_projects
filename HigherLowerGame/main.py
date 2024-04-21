# Higher Lower game
# Felix van Kerkhoven
# 01/10/2023

from art import logo, vs
import random
from game_data import data
import os
import time


## functions ##
# def check_answer():
#     if answer == 'a':
#         one = check_followers(person1) > check_followers(person2)
#         return one
#     if answer == 'b':
#         two = check_followers(person2) > check_followers(person1)
#         return two


def check_followers(person):
    followers_person = f"{person['follower_count']}"
    return followers_person


def format_person(person):
    formatted_person = f"{person['name']}, a {person['description']}, from {person['country']}"
    return formatted_person


# game
score = 0
Game_is_on = True
while Game_is_on:
    #choosing a person
    person1 = random.choice(data)
    person2 = random.choice(data)

    #printing
    print(logo)
    print("Compare A:\n", format_person(person1))
    print(vs)
    print("against B:\n", format_person(person2))

    print("Who has more followers?")
    answer = input("Type 'A' or 'B': ").lower()
    os.system("cls" if os.name == "nt" else "clear")
    print(logo)


    # checking answer
    if answer == 'a' and check_followers(person1) > check_followers(person2):
        print("You're right!")
        score = + 1
        print("Your score is", score)
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
    elif answer == 'b' and check_followers(person2) > check_followers(person1):
        print("You're right!")
        score = + 1
        print("Current score:", score)
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Sorry, that's wrong.")
        print(":((")
        print("Final score:", score)
        Game_is_on = False
    person2 = person1

# TODO: place option B as option A next round

#
# from art import logo, vs
# import random
# from game_data import data
# import os
#
# def format_person(person):
#     return f"{person['name']}, a {person['description']}, from {person['country']}"
#
# def random_person2(exclude_person):
#     person2 = random.choice(data)
#     while person2 == exclude_person:
#         person2 = random.choice(data)
#     return person2
#
# print(logo)
#
# score = 0
#
# while True:
#     person1 = random.choice(data)
#     print(f"Compare A: {format_person(person1)}")
#
#     print(vs)
#
#     person2 = random_person2(person1)
#     print(f"Against B: {format_person(person2)}")
#
#     answer = input("Who has more followers? Type 'A' or 'B': ").lower()
#     os.system("cls" if os.name == "nt" else "clear")
#
#     if answer == 'a' and person1['follower_count'] > person2['follower_count']:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     elif answer == 'b' and person2['follower_count'] > person1['follower_count']:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score: {score}")
#         break
