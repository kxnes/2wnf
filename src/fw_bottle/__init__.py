import bottle

from config import PING_MESSAGE


app = bottle.Bottle()


@app.route('/')
def ping():
    return PING_MESSAGE.format(app='bottle')
