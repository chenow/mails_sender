import os
import pandas as pd

from send_mail import *

if __name__ == "__main__":

    PASSWORD = os.getenv('PASSWORD')
    SENDER_MAIL = os.getenv("SENDER_MAIL")

    mails = pd.read_csv('mails.csv', sep=',')
    mails_to_send = []
    receivers_email_to = ''
    ent = mails['ent'].tolist()[0]

    for index, row in mails.iterrows():
        if (ent == row['ent'] or ent == ''):
            mails_to_send.append(row['mail'])
            receivers_email_to += row['mail'] + ', '
            ent = row['ent']
        else:
            file = open("TRACS_2022_rappel.html", "r")
            send_mail(file.read().replace('Bonjour', 'Bonjour ' + ent),
                      mails_to_send,
                      receivers_email_to,
                      sender_email=SENDER_MAIL,
                      password=PASSWORD,
                      pdfname='Plaquette TRACS 2022.pdf')
            ent = row['ent']
            mails_to_send = [row['mail']]
            receivers_email_to = row['mail'] + ', '
