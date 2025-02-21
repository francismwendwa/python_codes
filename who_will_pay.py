import random

name_string = input(" Enter names of all who have participated")
names = name_string.split(", ")

number_of_people = (len(names))

random_person = random.randint(0, number_of_people - 1)
person_to_pay = names[random_person]

print(f"Today, {person_to_pay} will pay the bill.")
