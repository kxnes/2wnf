import pyramid.config
import pyramid.response

from config import PING_MESSAGE


# noinspection PyUnusedLocal
def ping(request):
    return pyramid.response.Response(PING_MESSAGE.format(app='pyramid'))


with pyramid.config.Configurator() as config:
    config.add_route('ping', '/')
    config.add_view(ping, route_name='ping')
    app = config.make_wsgi_app()
