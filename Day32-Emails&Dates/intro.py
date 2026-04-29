import smtplib

my_email = "myemail@gmail.com"
password = "passs"

to= "toemail@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #encrypt messages
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to, msg="Subject:Hello\n\nThis is the body of my email") 


import datetime as dt

now = dt.datetime.now()

year = now.year

day_of_week = now.weekday()

if year == 2026:
    print("Oh jesus!")

print(now)
print(type(now))
print(year)
print(type(year))
print(day_of_week)
print(type(day_of_week))

date_of_birth = dt.datetime(year=1990, month=5, day=8, hour=6, minute=28)
print(date_of_birth)

