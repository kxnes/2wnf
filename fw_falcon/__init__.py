import falcon

from .middleware import AuthMiddleware, RequireJSONMiddleware, JSONTranslatorMiddleware
from .resources import HelloWorldResource, ThingsResource
from .storage import StorageEngine
from .errors import StorageError
from .adapters import SinkAdapter

app = falcon.API(middleware=[AuthMiddleware(), RequireJSONMiddleware(), JSONTranslatorMiddleware()])

app.add_route('/hw/', HelloWorldResource)
app.add_route('/{user_id}/things/', ThingsResource(StorageEngine()))
app.add_error_handler(StorageError, StorageError.handle)
app.add_sink(SinkAdapter(), r'/search/(?P<engine>google|yandex)\Z')
