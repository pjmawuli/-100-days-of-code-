student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Draco": 74,
    "Hermoine": 99,
    "Neville": 61,
}

student_grades = {}

for key, value in student_scores.items():
    if value >= 91 and value <= 100:
        value = "Outstanding"
    elif value >= 81 and value <= 90:
        value = "Exceeds Expectation"
    elif value >= 71 and value <= 81:
        value = "Acceptable"
    elif value < 71:
        value = "Fail"
        
    student_grades[key] = value


print(student_grades)