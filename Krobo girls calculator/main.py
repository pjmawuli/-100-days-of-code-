import pandas
import csv

data = pandas.read_csv("Sheets/1 ART 1E-C.R.S-DOKU  GIFTY-2021-2022-FIRST.csv")

thirty_p = []
seventy_p = []

for scores in data["Class_Work"]:
    thirty_p.append(round(scores * 0.3, 2))

print(thirty_p)

for scores in data["Exam_Score"]:
    seventy_p.append(round(scores * 0.7, 2))

print(seventy_p)


