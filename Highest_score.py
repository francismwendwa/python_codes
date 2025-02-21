print("Welcome to our highest score calculator calculator!!")

student_score = input("Enter your score").split()
for x in range(0, len(student_score)):
    student_score[x] = int(student_score[x])

highest_score = 0

for score in student_score:
    if score > highest_score:
        highest_score = score

print(highest_score)




