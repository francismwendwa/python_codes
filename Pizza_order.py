print(" Welcome to our pizza order!!")
size = input(" What size do you want to order? small, medium, or large?")
pepperoni = input(" Do you want to add pepperoni? yes or no?")
extra_cheese = input(" Do you want extra cheese? yes or no?")

bill = 0
if size == "small":
    bill += 1000
elif size == "medium":
    bill += 1500
else:
    bill += 2000

if pepperoni == "yes":
    if size == "small":
        bill += 300
    else:
        bill += 500

if extra_cheese == "yes":
    bill += 100

print(f"Dear customer you will pay ksh {bill}")

