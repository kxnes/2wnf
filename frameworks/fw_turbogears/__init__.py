import tg

from config import PING_MESSAGE


class Ping(tg.TGController):
    @tg.expose()
    def index(self):
        return PING_MESSAGE.format(app='turbogears')


config = tg.AppConfig(minimal=True, root_controller=Ping())
app = config.make_wsgi_app()
