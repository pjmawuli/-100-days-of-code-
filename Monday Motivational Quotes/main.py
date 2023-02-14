import datetime as dt
import random
import smtplib

EMAIL = "padijmain@gmail.com"
R_EMAIL = "padijreceiver@yahoo.com"
PASSWORD = "cyberpunk2077"
SMTP = "smtp.gmail.com"

day = dt.datetime.now().weekday()

with open("quotes.txt", mode="r") as quotes:
    lines = quotes.readlines()
    current_quote = random.choice(lines)
    print(current_quote)

if day == 0:
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=R_EMAIL, msg=f"Subject:Monday's Motivational Quote\n\n{current_quote}", )
