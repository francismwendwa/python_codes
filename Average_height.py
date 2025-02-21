print("Welcome to our average height calculator!!")

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

total_num_students = 0
for student in student_heights:
    total_num_students += 1

average_height = round(total_height / total_num_students)
print(average_height)