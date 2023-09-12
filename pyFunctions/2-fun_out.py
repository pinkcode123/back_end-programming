from random import randint


def play_game():
    computer_Number = randint(1, 10)
    chance =3
    while chance >=3:
         userNumber = int(input("Guess the Number$ ") )
         if userNumber == computer_Number:
             print("congratulations, you WON")
             break
         else:
            print("Am sorry you lost ,try again$ ")







play_game()
