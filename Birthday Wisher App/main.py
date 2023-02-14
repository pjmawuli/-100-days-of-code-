import pandas
import random
import smtplib
import datetime as dt
import pathlib

# CONSTANTS
EMAIL = "padijnmm@gmail.com"
PASSWORD = "cyberpunk2077"
SMTP_GMAIL = "smtp.gmail.com"
SMTP_YAHOO = "smtp.mail.yahoo.com"

# Saving the birthdays into a DataFrame object
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")

now_day = dt.datetime.now().day  # today's day
now_month = dt.datetime.now().month  # today's month

for birthday in birthdays_dict:  # Looping through the birthdays to see if today is one of them

    birthday_day = birthday["day"]  # the day of the person's birthday
    birthday_month = birthday["month"]  # the month of the person's birthday

    if now_day == birthday_day and now_month == birthday_month:
        letter = ""  # Our actual letter that is going to be sent

        # Now if today is a birthday we are first going to have to select a random letter template
        letter_index = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_index}.txt", mode="r") as letter_file:
            letter_content = letter_file.readlines()  # A list of the lines in the selected letter template

            for line in letter_content:
                line = line.replace("[NAME]", birthday["name"])

                letter += line  # The letter has been updated with the content and the name in place

        # MAIL MECHANISM #
        if "gmail" in birthday["email"]:  # Making sure the smtp is accurate for any mail we receive
            receiver_smtp = SMTP_GMAIL
        else:
            receiver_smtp = SMTP_YAHOO

        with smtplib.SMTP(receiver_smtp) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=birthday["email"], msg=letter)

