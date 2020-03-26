from vulcan import Vulcan
import pickle

def register(token, symbol, pin):

    token = input('Podaj token: ').strip()
    symbol = input('Podaj symbol: ').strip()
    pin = input('Podaj PIN: ').strip()

    if token and symbol and pin:
        certificate = Vulcan.register(token, symbol, pin)

        with open('cert.json', 'wb') as f:
            pickle.dump(certificate, f)
    else:
        raise ValueError


if __name__ == '__main__':
    register(token, symbol, pin)
