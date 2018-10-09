import logging

import falcon

from .hooks import max_body


# noinspection PyUnusedLocal,PyMethodMayBeStatic
class HelloWorldResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = 'Hello, world!'


class ThingsResource:

    def __init__(self, db):
        self.db = db
        self.logger = logging.getLogger(__name__)

    def on_get(self, request, response, user_id):
        print('request:', request)
        print('response:', response)
        print('user_id:', user_id)
        marker = request.get_param('marker') or ''
        limit = request.get_param_as_int('limit') or 50

        try:
            result = self.db.all(marker, limit)
        except Exception as ex:
            self.logger.error(ex)
            raise falcon.HTTPServiceUnavailable('Service Outage', 'Aliens have attacked our base!', 30)

        response.context['result'] = result
        response.set_header('Powered-By', 'Falcon')
        response.status = falcon.HTTP_200

    @falcon.before(max_body(64 * 1024))
    def on_post(self, request, response, user_id):
        print('request:', request)
        print('response:', response)
        print('user_id:', user_id)
        try:
            doc = request.context['doc']
        except KeyError:
            raise falcon.HTTPBadRequest('Missing thing', 'A thing must be submitted.')

        proper_thing = self.db.add(doc)
        response.status = falcon.HTTP_201
        response.location = f'/{user_id}/things/{proper_thing["id"]}/'
