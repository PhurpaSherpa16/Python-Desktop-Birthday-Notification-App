import datetime
import pandas as pd
from plyer import notification
import random
from wishes import wishes


def notification_popup(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\\Python\\Birthday Notification\\Files\\Bicon.ico",
        timeout=10
    )


# random wishes will get from wishes.py file
def get_wish(wish):
    wish = random.choice(wish)
    return wish


def birthday_wish():
    # extracting today dates
    today = datetime.datetime.now().strftime("%d-%m")

    # accessing excel file
    df = pd.read_excel("D:\\Python\\Birthday Notification\\Files\\birthdates.xlsx")

    # extracting and matching condition if today dates == birthdates
    for index, item in df.iterrows():

        # this will show the list of birthdates if you print birthdate
        birthdate = item["Dates"]

        fo_for = item["FamousFor"]

        if today == birthdate:
            birthday_person_name = item["Names"]
            notification_popup("Birthday Notification", f"Today is birthday of {birthday_person_name}."
                                                        f"\nA {fo_for}."
                                                        f"\n{get_wish(wishes)}" 
                                                        # accessing get_wish Function and parsing parameter
                                                        f"\nThank You!!!")


if __name__ == '__main__':
    birthday_wish()
