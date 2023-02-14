student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [35, 75, 24],
}

# Looping through values in dictionary
# for key, value in student_dict.items():
#     print(f"{key}: {value}")

import pandas

students_dataFrame = pandas.DataFrame(student_dict)
# print(students_dataFrame)

# Looping through a dataframe
for index, value in students_dataFrame.iterrows():
    if value.student == "Angela":
        print(value.score)
