import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import os
load_dotenv()

URL = "https://www.amazon.sa/-/en/HyperX-Cloud-III-Ultra-Clear-USB/dp/B0C3BV19Q3?crid=OZNZA0AHV4B7&dib=eyJ2IjoiMSJ9.4YzDQ9OOtlBMumbC7JVO7lehobJOR-hLrTHQpkENlia9fdd31iyEKzDqNesFpvSQ6aV_cT3j2lbUSkthYX_0C9msZvuQdXXNmRkUALYTAchlqjKTHkRehfoevAUDibEsh350yrwI-slycJz7hhZ2xv7e1kqHqhz0rLL6NgQ50enrmv29JYxYBpfDhjPIlNOMH-awlWn0FGqTY5eRGJ3Yp5s5U3X49edofJ-32fRujcBNI6cItiOUqfpO5rL2ud-u8gEcy8wlpR_OUvaoUKqiriXaQuVf1p86SAXcgqhkZvU.NacD_bLcxLB_15G5p4gu9EnG9fLNSP3FwWwQ9pUVe8U&dib_tag=se&keywords=headset&qid=1773431972&sprefix=%2Caps%2C194&sr=8-13&th=1"
HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
whole_price = soup.find(name="span", class_="a-price-whole")
fraction_price = soup.find(name="span", class_="a-price-fraction")
price = float(whole_price.text + fraction_price.text)


with open("file.text", "r") as fp:
    if price < 200:
        my_email = os.getenv("FROM_EMAIL")
        password = os.getenv("FROM_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=os.getenv("RECEIVER_EMAIL"),
                msg = "Subject: Price Drop Alert! \n\nGood news! The HyperX Cloud III Wired Gaming Headset for PC is now on sale.",
            )




