import responder

from config import PING_MESSAGE


app = responder.API()


# noinspection PyUnusedLocal
@app.route('/')
def ping(req, resp):
    resp.text = PING_MESSAGE.format(app='responder')
