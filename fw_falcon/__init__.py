import falcon


from wsgiref import simple_server

from .middleware import AuthMiddleware, RequireJSONMiddleware, JSONTranslatorMiddleware
from .resources import HelloWorldResource
from .storage import StorageEngine


application = falcon.API(
    middleware=(AuthMiddleware, RequireJSONMiddleware, JSONTranslatorMiddleware)
)

db = StorageEngine()

application.add_route('/hw/', HelloWorldResource())
