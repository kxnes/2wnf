import cherrypy

from config import PING_MESSAGE


class Ping:
    @cherrypy.expose
    def index(self):
        return PING_MESSAGE.format(app='cherrypy')


cherrypy.tree.mount(Ping())
