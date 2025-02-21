print(" Welcome to our love calculator")

name_1 = input(" What is the first name?")
name_2 = input(" What is the second name?")

combined_name = name_1 + name_2
new_combined_name = combined_name.lower()

t = new_combined_name.count("t")
r = new_combined_name.count("r")
u = new_combined_name.count("u")
e = new_combined_name.count("e")

true = (t + r + u + e)

l = new_combined_name.count("l")
o = new_combined_name.count("o")
v = new_combined_name.count("v")
e = new_combined_name.count("e")

love = (l + o + v + e)

cal_name = int(str(true) + str(love))

if cal_name <= 10 or cal_name >= 90:
    print(f"your love score is {cal_name} you go together like coke and mentos")
elif cal_name <= 50 or cal_name >= 40:
    print(f'Your score is {cal_name} you are alright together')
else:
    print(f'your score is {cal_name} ')


print(cal_name)
