# MAILS_SENDER

This project aims at sending emails to a list of recipients. It is based on a
SMTP connection to a mail box using a pair of email and password. Emails will be sent
from this mail box to the recipients, with the email provided as the sender.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

- complete the .env following the .env.template file format.
- Put the list of recipients in the users folder, following the users/example.csv template.
- Add a HTML design for the mail, similar to the templates/example.html file. Variables
  can be added to the template, and will be replaced by the values in the csv file.

- [Optional] add an attached file to the mail, by adding it to the attachments folder.

Then, run the main.py file:

```bash
    python main.py
```
