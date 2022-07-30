# This program tells you the maximum value in a given list of numbers


# Changing the string of the list into a list of integers
student_scores = input("Type in the scores of your useless students  ").split();
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n]);

# Determining the highest value
highest_value = 0;
for score in student_scores:
    if score >= highest_value:
        highest_value = score;

print(f"The highest score in the list of scores is {highest_value}.");