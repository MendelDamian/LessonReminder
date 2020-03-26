from vulcan import Vulcan
import pickle

def login():

    with open('cert.json', 'rb') as f:
        certificate = pickle.load(f)

    client = Vulcan(certificate)

    return client
