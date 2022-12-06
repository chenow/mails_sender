from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import time

def send_mail(body, receivers_email, receivers_email_to, sender_email=None, password=None, pdfname=None):
    mailobj = smtplib.SMTP('smtp-mail.outlook.com', 587)
    mailobj.ehlo()
    mailobj.starttls()
    mailobj.login(sender_email, password)

    msg = MIMEMultipart()
    msg['Subject'] = 'Rappel - invitation TRACS 2022'
    msg['From'] = sender_email
    msg['To'] = receivers_email_to
    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)
    binary_pdf = open(pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    #payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    msg.attach(payload)
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(sender_email, password)
            smtpObj.sendmail(sender_email, receivers_email, msg.as_string())
            print("mail sent")
    except Exception as e:
        print(e)

    mailobj.quit()
    time.sleep(2)
    return
