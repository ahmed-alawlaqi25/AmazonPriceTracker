import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import os
load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
whole_price = soup.find(name="span", class_="a-price-whole")
fraction_price = soup.find(name="span", class_="a-price-fraction")
price = float(whole_price.text + fraction_price.text)

with open("file.text", "r") as fp:
    if price < 100:
        my_email = os.getenv("FROM_EMAIL")
        password = os.getenv("FROM_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.getenv("RECEIVER_EMAIL"),
                msg="Subject:Big Sales \n\nInstant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker. Is on Sale go GET one.",
            )

