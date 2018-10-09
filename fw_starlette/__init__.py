from starlette.applications import Starlette
from starlette.responses import HTMLResponse


app = Starlette()


# noinspection PyUnusedLocal
@app.route('/hw/')
def hello_world(request):
    return HTMLResponse('Hello, world!')
