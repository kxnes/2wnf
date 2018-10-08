import falcon


# noinspection PyUnusedLocal
class StorageError(Exception):

    @staticmethod
    def handle(exception, request, response, params):
        print('exception:', exception)
        print('request:', request)
        print('response:', response)
        print('params:', params)
        # fixme: what's the hell
        raise falcon.HTTPError(falcon.HTTP_740, 'Database Error', falcon.HTTP_799)
