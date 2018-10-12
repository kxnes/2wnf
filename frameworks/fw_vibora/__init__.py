import vibora

from config import PING_MESSAGE


app = vibora.Vibora()


@app.route('/')
async def home():
    return vibora.Response(PING_MESSAGE.format(app='vibora').encode())
