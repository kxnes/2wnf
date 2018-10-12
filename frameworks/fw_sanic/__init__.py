import sanic
import sanic.response

from config import PING_MESSAGE


app = sanic.Sanic()


# noinspection PyUnusedLocal
@app.route('/')
async def ping(request):
    return sanic.response.text(PING_MESSAGE.format(app='sanic'))
