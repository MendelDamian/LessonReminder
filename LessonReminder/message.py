from fbchat import Client
from fbchat.models import *
import os


def message(text):
    email = os.environ['E-MAIL']
    password = os.environ['FBPASSWORD']
    thread_type = ThreadType.USER
    client = Client(email, password)

    if not client.isLoggedIn():
        client.login(email, password)

    client.send(Message(text=text), thread_id=client.uid, thread_type=thread_type)
