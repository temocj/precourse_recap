# Copyright 2020 Temoc
# TODO: add multiplayer betting system

import random

rand_n = int(random.random() * 100)

lower = rand_n - 1 - int(random.random() * 2)
upper = rand_n + 1 + int(random.random() * 2)

answer = input("Guess the random number between " \
    + str(lower) + " and " + str(upper) + ": ")

guesses = 1
max_guesses = upper - lower - 1

while answer != str(rand_n):
    answer = input("Try again: ")
    guesses += 1

if guesses == 1:
    print("Aren't you lucky!")
elif guesses == max_guesses:
    print("You finally got it!")
else:
    print("Correct!")