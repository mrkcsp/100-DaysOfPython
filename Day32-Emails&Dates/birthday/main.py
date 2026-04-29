import smtplib
import datetime as dt
import random
import pandas

email = "test@email.com"
password = "pass"
birthdays_file = "birthdays.csv"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv(birthdays_file)

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, "r") as template:
        template_letter = template.read()
        new_template = template_letter.replace("[NAME]", birthday_person["name"], -1)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{new_template}")


