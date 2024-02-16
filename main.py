import smtplib
import pandas
from datetime import datetime
import random



today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for index, data_row in data.iterrows()}




if (today_tuple) in birthdays_dict:
    birthdays_person=birthdays_dict[today_tuple]
    filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath,"r") as text:
        contents = text.read()
        contents.replace("[NAME]",birthdays_person["name"])
    with smtplib.SMTP("smtp.gmail.com",port=587) as connect:
        connect.starttls()
        connect.login("yourmail@gmail.com","yourpass")
        connect.sendmail(from_addr="yourmail@gmail.com",
                         to_addrs=birthdays_person["email"],
                         msg=f"Subject:happy birthday\n\n{contents}")