import json

from vulcan import Vulcan


def register(token=None, symbol=None, pin=None):
    if not token:
        token = input('Podaj token: ').strip()
    if not symbol:
        symbol = input('Podaj symbol: ').strip()
    if not pin:
        pin = input('Podaj PIN: ').strip()

    if token and symbol and pin:
        certificate = Vulcan.register(token, symbol, pin)

        with open('cert.json', 'w') as f:
            json.dump(certificate.json, f)
    else:
        raise ValueError


if __name__ == '__main__':
    register()
