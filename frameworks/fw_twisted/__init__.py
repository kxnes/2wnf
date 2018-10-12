from twisted.web import server, resource

from config import PING_MESSAGE


class Ping(resource.Resource):
    isLeaf = True

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def render_GET(self, request):
        request.setHeader(b'content-type', b'text/plain')
        return PING_MESSAGE.format(app='twisted').encode('utf-8')


app = server.Site(Ping())
