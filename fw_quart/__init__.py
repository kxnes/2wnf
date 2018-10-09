from quart import Quart


app = Quart(__name__)


@app.route('/hw/')
async def hello_world():
    return 'Hello, world!'
