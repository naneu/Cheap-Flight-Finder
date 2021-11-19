import requests
import smtplib
from twilio.rest import Client

my_email = ""
password = ""
account_sid = ""
auth_token = ""

class NotificationManager:
    def __init__(self):
        self.client =  Client(account_sid, auth_token)
    #This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, message):
        
        message = self.client.messages.create(
            body=message,
            from_='',
            to=''
        )

    def send_emails(self,emails,message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(
                from_addr=my_email,
                to_addrs=emails,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
            )
