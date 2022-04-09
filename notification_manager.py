from twilio.rest import Client
import os
class NotificationManager:
    def send_message(self, price, destination, location):
        client = Client(os.environ["account_sid"], os.environ['auth_token'])
        message = client.messages \
            .create(
            body=f"Flight from {location}, to {destination} for only ${price}️",
            from_='+12073869879',
            to='+1##########'
        )
        print(message.status)
