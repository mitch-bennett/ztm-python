import random
import sys

# sys.argv[0]

# start and end for args
# randomly generate number
# user input until true

low = sys.argv[1]
high = sys.argv[2]
number = random.randint(low, high)

while True:
    guess = int(input(f'Guess a number between {low} and {high}!'))
    if guess == number:
        break
