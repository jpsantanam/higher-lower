from art import logo, vs
from game_data import data
from random import choice
import os


def formatData(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def calcHigher(a, b):
    if a > b:
        return 'a'
    else:
        return 'b'


def main():
    clear = lambda: os.system('cls')
    isOver = False
    score = 0
    accountB = choice(data)

    print(logo)

    while not isOver:
        accountA = accountB
        accountB = choice(data)
        while accountB == accountA:
            accountB = choice(data)
        followersA = accountA["follower_count"]
        followersB = accountB["follower_count"]
        higher = calcHigher(followersA, followersB)

        print(f"Compare A: {formatData(accountA)}.")
        print(vs)
        print(f"Against B: {formatData(accountB)}.")

        userGuess = input("Who has more followers? Type 'A' or 'B': ").lower()

        clear()
        print(logo)

        if higher != userGuess:
            isOver = True
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            score += 1
            print(f"You're right! Current: {score}")


if __name__ == "__main__":
    main()
