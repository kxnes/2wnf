import flask

from config import PING_MESSAGE


app = flask.Flask(__name__)


@app.route('/')
def ping():
    return PING_MESSAGE.format(app='flask')
