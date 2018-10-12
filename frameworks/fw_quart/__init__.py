import quart

from config import PING_MESSAGE


app = quart.Quart(__name__)


@app.route('/')
async def ping():
    return PING_MESSAGE.format(app='quart')
