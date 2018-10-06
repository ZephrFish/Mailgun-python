# Send Mail with Mailgun using API
# Used for sending emails
# Setup: Replace your sending email for mailgun in FROM and recipient email in TO, the script takes subject and message as input
# Replace APIKEYHERE with your mailgun APIkey.
# Replace YOURDOMAINHERE with your mailgun domain.

import requests
import sys

def sendEmail(subject, message):

    files = {
            'from': (None, 'EXAMPLE Sender <EMAILADDRESS>'),
            'to': (None, 'EXAMPLE Recipient <blah@blah.com>'),
            'subject': (None, subject),
            'text': (None, message),
    }

    response = requests.post('https://api.mailgun.net/v3/YOURDOMAINHERE/messages', files=files, auth=('api', 'APIKEYHERE'))

# Entry point, expecting to be called ./sendEmail.py <subject> <message>
if __name__ == '__main__':
    sendEmail(sys.argv[1], sys.argv[2])
