import random

randomN = int(random.random() * 100)

rand_lower = 1 + int(random.random() * 2)
rand_upper = 1 + int(random.random() * 2)

lower = randomN - rand_lower
upper = randomN + rand_upper

while True:
    answer = input("Guess the random number between " + str(lower) + " and " + str(upper) + ": ")
    if answer == str(randomN):
        print("Correct!")
        break
    else:
        print("Try again!")