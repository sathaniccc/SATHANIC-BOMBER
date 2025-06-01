import os
import random
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('AC9df72adf5c5f8dcfc7c0fe28eb885dea')
auth_token = os.getenv('85d31daf30769cd327e170c6d32f8ef8')
twilio_number = os.getenv('918921016567')
target_number = os.getenv('918921016567')

client = Client(account_sid, auth_token)

otp = str(random.randint(100000, 999999))
message = client.messages.create(
    body=f'Your OTP is {otp}',
    from_=twilio_number,
    to=target_number
)

print(f"[✔] OTP sent to {target_number} → SID: {message.sid}")
