from random import randint
computer_Number = randint(1, 10)


def play_game():
    chance = 0
    while chance < 3:
        userNumber = int(input("Guess the Number$ "))
        if userNumber == computer_Number:
            print("congratulations, you WON")
            break
        else:

            print("Am sorry you lost ,try again$ ")


play_game()
