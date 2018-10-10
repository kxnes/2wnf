import weppy

from config import PING_MESSAGE


app = weppy.App(__name__)


@app.route('/')
def ping():
    return PING_MESSAGE.format(app='weppy')
