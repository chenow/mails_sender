import os
import pandas as pd
from dotenv import load_dotenv


from send_mail import send_mail

load_dotenv()

PASSWORD = os.getenv("PASSWORD")
SENDER_MAIL = os.getenv("SENDER_MAIL")
USERS = os.getenv("users")
TEMPLATE = os.getenv("template")
ATTACHED_FILE = os.getenv("attached_file")


def main():
    users = pd.read_csv("mails.csv", sep=",")
    for index, row in users.iterrows():
        print(f"{index + 1 } / {len(users)} Sending mail to {row['email']}...")
        file = open(TEMPLATE, "r")
        send_mail(
            file.read().replace("Bonjour", "Bonjour " + row["name"]),
            row["email"],
            f"{row['email']},",
            sender_email=SENDER_MAIL,
            password=PASSWORD,
            pdfname=ATTACHED_FILE.split("/")[-1],
        )


if __name__ == "__main__":
    main()
