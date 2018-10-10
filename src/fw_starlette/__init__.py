import starlette.applications
import starlette.responses

from config import PING_MESSAGE


app = starlette.applications.Starlette()


# noinspection PyUnusedLocal
@app.route('/')
def ping(request):
    return starlette.responses.HTMLResponse(PING_MESSAGE.format(app='starlette'))
