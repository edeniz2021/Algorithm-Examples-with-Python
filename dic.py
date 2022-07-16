student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}


for i in student_scores:
    a = student_scores[i]
    if a > 91 and a<=100:
        student_grades[i] = "Outstanding"
    elif a > 81 and a <= 90:
        student_grades[i] = "Exceeds Expectations"
    elif a > 71 and a <= 80:
        student_grades[i] = "Acceptable"
    else:
        student_grades[i] = "Fail"


print(student_grades)