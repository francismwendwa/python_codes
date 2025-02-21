print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side_choice = input("Which side do you want to go? right or left?")
if side_choice == "left":
    another_choice = input("you have come to a golden door. Upon opening there is a lake. do you chose to swim or wait?")
    if another_choice == "swim":
        print("You are dead and crocodiles have had their christmas")
    elif another_choice == "wait":
        color = input("you get to chose a color. red, blue or green")
        if color == "red":
            print("Red means danger. you are out")
        elif color == "green":
            print("You thought green was greener pastures. think again. You are out")
        else:
            print(" you have found the treasure")


else:
    choice = input("You have entered the lions den. do you chose a knife or gun?")
    if choice == "gun":
        print("wrong choice. you are dead")
    else:
        print(" A knife is never the safest option. you got shot")