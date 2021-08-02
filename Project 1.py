# Angelo Lapponese Treehouse Project 1
import random

# Introduction
print("------ Welcome to Angelo's Super Special Number Guessing Game! ------")
user_name = input("What is your name?  ")

# This part gave me the most trouble. I didn't know how to get this variable to be used inside the function.
# I kept getting an error that said "referenced before assignment". I googled it and found that i need to
# label this a global variable inside my function. The website I got this answer from is:
# https://stackoverflow.com/questions/855493/referenced-before-assignment-error-in-python

highscore = int(9999999)

def start_game():
    num_of_guesses = 1
    win_num = random.randint(1,10)
    num_guess = int(987654321)
    global highscore
    print("\nOkay {},".format(user_name))
    while num_guess != win_num:
        try:
        # The part that kept messing me up where to put the user input line.
        # I put it right after the "try" statement and everything ran smoothly after that.
            num_guess = int(input("Pick a number between 1 and 10: "))
            if num_guess < 1 or num_guess > 10:
                print("I'm sorry, but that guess is outside the allowed range of answers!")
                num_of_guesses += 1
            elif num_guess > win_num and num_guess < 11:
                print("I'm sorry {}, but that guess is too high...".format(user_name))
                num_of_guesses += 1
            elif  num_guess < win_num and num_guess > 0:
                print("I'm sorry {}, but that guess is too low...".format(user_name))
                num_of_guesses += 1
        except ValueError:
            print("The number must be an integer between 1 and 10! ")
            num_of_guesses += 1
    else:
        print("""\nCongrats {}! The number was {}!
You guessed the correct answer and it only took {} tries!\n""".format(user_name, win_num, num_of_guesses))
        if num_of_guesses < highscore:
            highscore = num_of_guesses
        else:
            print("Sorry but you did not break the highscore of {}...\n".format(highscore))

start_game()
replay = "yes"
while replay == "yes":
    replay = input("Would you like to play again? ")
    if replay.lower() == "yes":
        start_game()
    else:
        print("Thanks for playing! The high score is {}!".format(highscore))
        exit()
else:
    exit()
    

