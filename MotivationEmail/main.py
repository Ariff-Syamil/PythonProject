import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = "mohammadx.ariff.syamil.bin.idrus@intel.com"
password = "AngahBoring9%"
receiver_email = "mohdsyamil95@gmail.com"
Subject = "MotivationMonday"

with open("quotes.txt", "r",encoding='utf-8') as file:
    quotes = file.readlines()
    word_quote = [quote.strip() for quote in quotes]
quote_of_the_day = random.choice(word_quote)

message = MIMEMultipart()
message["From"] = email
message["To"] = receiver_email
email_quote = message.attach(MIMEText(quote_of_the_day,'plains', _charset="utf-8"))

with smtplib.SMTP("smtpauth.intel.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(email, receiver_email
        ,f"""\

        {email_quote}
        """
    )
print("Email sent successfully!")
