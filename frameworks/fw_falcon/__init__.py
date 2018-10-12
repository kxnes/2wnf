import falcon

from config import PING_MESSAGE


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class Ping:
    def on_get(self, request, response):
        response.status, response.body = falcon.HTTP_200, PING_MESSAGE.format(app='falcon')


app = falcon.API()
app.add_route('/', Ping())
