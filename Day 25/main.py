import pandas

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.DictReader(data_file)
#     temperatures = []
#
#     # for row in data:
#     #     print(row[1])
#
#     for temperature in data:
#         temperatures.append(int(temperature["temp"]))
#
#     print(temperatures)


# Here is the pandas function that lets us read csv data
data = pandas.read_csv("weather-data.csv")
#
# # And this here is the function that lets us change the DataFrame object into a dictionary
# data_dict = data.to_dict()
#
# # And this here lets us change the series object into a list
# data_temperature = data["temp"]
# data_list = data_temperature.to_list()
#
# print(f"The average of the temperatures = {round(sum(data_list) / len(data_list), 2)}")
# # OR
# print(f"The average of the temperatures = {round(data_temperature.mean(), 2)}")
# print(f"The maximum temperature is = {data_temperature.max()}")
#
# # Get Data in column
# print(data["condition"])
# print(data.condition)

# Get Data in row
# max_temp = max(data["temp"])
# print(data[data.temp == max_temp])

# Getting specific data from a sliced file
# monday = data[data.day == "Monday"]
# # We're converting the temperature from celsius to fahrenheit
# c_temp = int(monday.temp)
# f_temp = (c_temp * 9/5 + 32)
# print(f_temp)

# Create a Dataframe from scratch
student_dic = {
    "Names": ["Naruto", "Sakura", "Sasuke", "Goku"],
    "Scores": [6, 7, 9, 10],
}

data = pandas.DataFrame(student_dic)
print(data)

# From pandas to csv:
data.to_csv("students.txt")
