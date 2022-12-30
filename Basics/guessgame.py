from random import randint
import sys

# generate a number 1~10
answer = randint(1, 5)


def fcnGuess(guess, answer):
    if 0 < guess < 6:
        if guess == answer:
            print("you are a genius!")
            return True
            # sys.exit()
    else:
        print("hey bozo, I said 1~5")
        return False


# input from user?
# check that input is a number 1~10
if __name__ == "__main__":
    while True:
        try:
            guess = int(input("guess a number 1~5:  "))
            if fcnGuess(guess, answer):
                break
        except ValueError:
            print("please enter a number")
            continue
