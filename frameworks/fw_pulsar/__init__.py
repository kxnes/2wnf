import pulsar.apps.wsgi

from config import PING_MESSAGE


class Ping(pulsar.apps.wsgi.Router):
    # noinspection PyUnusedLocal,PyMethodMayBeStatic
    def get(self, request):
        return pulsar.apps.wsgi.WsgiResponse(200, PING_MESSAGE.format(app='pulsar'))


app = pulsar.apps.wsgi.handlers.WsgiHandler((Ping('/'), ))
