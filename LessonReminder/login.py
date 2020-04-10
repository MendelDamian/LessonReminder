import json
from vulcan import Vulcan


def login():
    with open('cert.json', 'r') as f:
        certificate = json.load(f)

    client = Vulcan(certificate)

    return client
