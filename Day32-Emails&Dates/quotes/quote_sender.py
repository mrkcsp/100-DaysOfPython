import smtplib
import datetime as dt
import random

email = "fromemail@gmail.com"
to = "toemail@hotmail.it"
password = "nbgogutwsjmuarqq"
quote_file = "quotes.txt"

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to, msg=f"Subject:Start your week with superpowers\n\n{choose_quote()}")


def choose_quote():
    with open(quote_file, "r") as file:
        data = file.readlines()
        random_quote = data[random.randint(0, len(data) - 1)]
        #print(type(data))
        #print(len(data))
        return random_quote
        

now = dt.datetime.now()
#print(now.weekday())
if now.weekday() == 0:
    print("It's monday, I'll send the quote!")
    send_email()
    print("Email sent!")
else: 
    print("Today is not monday :(")

