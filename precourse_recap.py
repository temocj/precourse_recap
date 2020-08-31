import random

rand_n = int(random.random() * 100)

lower = rand_n - 1 - int(random.random() * 2)
upper = rand_n + 1 + int(random.random() * 2)

answer = input("Guess the random number between " \
    + str(lower) + " and " + str(upper) + ": ")

while answer != str(rand_n):
    answer = input("Try again: ")

print("Correct!")