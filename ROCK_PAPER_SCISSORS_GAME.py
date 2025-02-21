import random

print("Welcome to our rock paper scissors game!!")

users_choice = input( "please type 0 for rock, 1 for paper and 2 for scissors. \n")


computers_choice = str(random.randint(0, 2))

if computers_choice == 2 and users_choice == 0:
    print(" you win!! ")
elif computers_choice > users_choice:
    print(" You lose!! ")
elif computers_choice == users_choice:
    print(" Its a draw. please repeat again.")
else:
    print(" You win")
