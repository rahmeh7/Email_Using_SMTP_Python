import smtplib
import os
import json
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow


# set up OAuth 2.0 credentials
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/gmail.send'])
if not creds or not creds.valid:
    with open('credentials.json', 'r') as f:
        client_config = json.load(f)['installed']
    flow = InstalledAppFlow.from_client_config(client_config, ['https://www.googleapis.com/auth/gmail.send'])
    creds = flow.run_local_server(port=0)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# create the message object
msg = EmailMessage()
msg['From'] = 'rahulmehta.rm933@gmail.com'
msg['To'] = 'rmehta.r7@gmail.com'
msg['Subject'] = 'Test email'
msg.set_content('This is a test email.')

# send the email using SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(creds.token, None)
    smtp.send_message(msg)
