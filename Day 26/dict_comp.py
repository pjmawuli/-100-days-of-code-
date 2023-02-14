# Studying dictionary comprehensions
import random

students = ['Alex', 'Beth', 'Caroline', 'Dave', 'Frieda']
students_scores = {student: random.randint(0, 100) for student in students}
print(students_scores)

passed_students = {student: score for student,score in students_scores.items() if score > 60}
print(passed_students)