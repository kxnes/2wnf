import molten

from config import PING_MESSAGE


def ping():
    return PING_MESSAGE.format(app='molten')


app = molten.App(routes=[molten.Route('/', ping)])
