import yagmail
import json
import os

class Messenger:
    def __init__(self):
        self.user = 'kylethescientist@gmail.com'
        self.app_password = 'uecaifbcqrmipuam'
        filepath = f'{os.path.dirname(os.path.realpath(__file__))}/users.json'
        with open(filepath, 'r') as f:
            self.recipients = json.loads(f.read())

    def send(self, text):
        try:
            with yagmail.SMTP(self.user, self.app_password) as yag:
                for recipient in self.recipients.values():
                    yag.send(recipient, "", text)
        except Exception as e:
            print('Email failed to send')

