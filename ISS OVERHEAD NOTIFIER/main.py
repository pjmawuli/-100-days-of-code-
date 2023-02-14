import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 180.507351  # MY latitude
MY_LONG = 0.127758  # MY longitude


def check_location():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    my_lat = {
        "low_bound": MY_LAT - 5,
        "high_bound": MY_LAT + 5,
    }
    my_long = {
        "low_bound": MY_LONG - 5,
        "high_bound": MY_LONG + 5,
    }

    if my_lat["high_bound"] > MY_LAT > my_lat["low_bound"] and my_long["high_bound"] > MY_LONG > my_long["low_bound"]:
        return True

    # checking if my position is within +5 or -5 degrees of the ISS position.


is_close = check_location()

if is_close:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    def check_time():
        time.sleep(60)
        suns_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        suns_response.raise_for_status()
        suns_data = suns_response.json()
        sunrise = int(suns_data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(suns_data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        current_hour = time_now.hour

        if sunrise < current_hour < sunset:
            return True
    while True:
        if check_time():
            MY_EMAIL = "padijnmm@gmail.com"
            MY_PASSWORD = "Cyberpunk2077."
            SMTP_GMAIL = "smtp.gmail.com"
            RECIEVER_EMAIL = "jnmpadi@st.ug.edu.gh"

            msg = "The ISS is OVERHEAD!!!!"
            with smtplib.SMTP(SMTP_GMAIL) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIEVER_EMAIL, msg=f"Subject:LOOK UP!! \n\n {msg}",)
