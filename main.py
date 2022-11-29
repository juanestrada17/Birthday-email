import pandas
import smtplib
import datetime as dt
from random import choice
import sys

# TODO 1. Update the birthdays.csv

birthdays = pandas.read_csv("birthdays.csv")

# TODO 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day

# access the person with the two conditions
try:
    selected_birth = birthdays[(birthdays.month == month) & (birthdays.day == day)]
    name = selected_birth.to_dict()["name"][1]
except KeyError:
    print("Today's no one's birthday")
    sys.exit(1)



# TODO 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
#  with the person's actual name from birthdays.csv
files_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = choice(files_list)


with open(f"letter_templates/{random_letter}") as data:
    letter = data.read()
    new_letter = letter.replace("[NAME]", f"{name}")


# TODO 4. Send the letter generated in step 3 to that person's email address.

my_email = "testinmail17@gmail.com"
password = "testers17"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=selected_birth.to_dict()["email"][1],
                            msg=f"Subject: Happy birthday {name}!\n\n{new_letter}")

