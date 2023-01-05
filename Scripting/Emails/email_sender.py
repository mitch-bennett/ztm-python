# python has a built in email module
# resources:
# https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp
# https://docs.python.org/3/library/email.examples.html
# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/


# applications: personalized email from business, or automated email from self

# smtp = simple mail transfer protocol. needed for server connections
# suggested ports are 587 or 465 per google
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


# pwd generated from google settings > app passwords
# ukxnwmjsarbdnaqi

# use Path to access html file, then use string Template to parse
html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "Mitch Bennett"
email["to"] = "mitch.f.bennett@gmail.com"
email["subject"] = "You won 1,000,000 dollars!"
email.set_content("I am a Python Master!")

email.set_content(html.substitute({"name": "TinTin"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("mitch.f.bennett@gmail.com", "ukxnwmjsarbdnaqi")
    smtp.send_message(email)
    print("all good boss!")


# other examples from stack overflow

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
#     email_address = 'your_email_sender@gmail.com'
#     email_password = 'App_Passwords_is_generated'
#     connection.login(email_address, email_password )
#     connection.sendmail(from_addr=email_address, to_addrs='receiver_email@something.com',
#     msg="subject:hi \n\n this is my message")


# connection = smtp.SMTP_SSL('smtp.gmail.com', 465)

# email_addr = 'my_email@gmail.com'
# email_passwd = 'app_password_generated_in_Google_Account_Settings'
# connection.login(email_addr, email_passwd)
# connection.sendmail(from_addr=email_addr, to_addrs='recipient@something.com', msg="Sent from my IDE. Hehe")
# connection.close()
