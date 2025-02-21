print("Welcome to our even and odd calculator!!")

target = int(input("Enter the number up to which you would like to calculate. 1 to ?"))
answer = input("Which type would you like to know. odd or even?")

total_number = 0
if answer == "even":
    for number in range(2, target + 1, 2):
        total_number += number
else:
    for number in range(1, target + 1, 2):
        total_number += number

print(total_number)

