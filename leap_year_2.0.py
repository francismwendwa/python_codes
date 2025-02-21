print(" Welcome to our leap year calculator !!")

year = int(input(" What is the year you want to know?"))

leap_year_1 = (year % 4)
leap_year_2 = (year % 100)
leap_year_3 = (year % 400)

if leap_year_1 == 0:
    if leap_year_2 == 0:
        if leap_year_3 == 0:
            print(" This is a leap year")
        else:
            print(" This is not a leap year")
    else:
        print(" This is a leap year")
else:
    print(" This is not a leap year")