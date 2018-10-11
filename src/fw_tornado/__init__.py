import tornado.web
import tornado.ioloop

from config import PING_MESSAGE, DEBUG, RELOAD


class Ping(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write(PING_MESSAGE.format(app='tornado'))


app = tornado.web.Application(debug=DEBUG, autoreload=RELOAD, handlers=[
    (r"/", Ping)
])
