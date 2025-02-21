import random

print("Welcome to our heads or tail calculator")
coin_tossed = input("Do you want to toss a coin. yes or no?")


if coin_tossed == "yes":
    coin_tossed = random.randint(1, 2)
    if coin_tossed == 1:
        print("Heads")
    else:
        print("Tails")
else:
    print("coin not tossed. GOODBYE!!")
