import random
import sys

# sys.argv[0]

# start and end for args
# randomly generate number
# user input until true

# low = int(sys.argv[1])
# high = int(sys.argv[2])
low = 1
high = 10
number = random.randint(low, high)

while True:
    guess = int(input(f"Guess a number between {low} and {high}:   "))
    try:
        if guess == number:
            print("great guess!")
            break
    except ValueError:
        print("number, please")
        continue
