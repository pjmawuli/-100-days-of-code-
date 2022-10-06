# This program asks for a list of student's heights and calculates the average of the list

# This block of code takes in a string of numbers and converts it into a list of numbers
student_heights = input("Type in the list of the student's heights whose averages you want to calculate: \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# This for loop calculates the number of students in a given list
num_of_students = 0
for num in student_heights:
    num_of_students += 1

# The total of the list of heights
total_students = 0
for x in student_heights:
    total_students = total_students + x

# The average
average = total_students / num_of_students
print(f"The average of the heights of the students is: {average}.");
