from wheezy.http import HTTPResponse, WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory

from config import PING_MESSAGE


class Ping(BaseHandler):
    def get(self):
        response = HTTPResponse()
        response.write(PING_MESSAGE.format(app='wheezyweb'))
        return response


app = WSGIApplication(
    middleware=[
        bootstrap_defaults(
            [
                url('', Ping)
            ]
        ),
        path_routing_middleware_factory
    ],
    options={}
)
