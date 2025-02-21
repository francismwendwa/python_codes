def life_in_weeks(age):
    current_age = int(input("how old are you?"))
    life_left = 90 - int(current_age)

    life_left_in_weeks = int(life_left) * 52

    print(f"You have {life_left_in_weeks} weeks left")


life_in_weeks(12)

