import requests


class SinkAdapter(object):

    engines = {
        'google': 'https://www.google.com/',
        'yandex': 'https://www.yandex.ru/'
    }

    def __call__(self, request, response, engine):
        print('request:', request)
        print('response:', response)
        print('engine:', engine)
        url = self.engines[engine]
        params = {'q': request.get_param('q', True)}
        result = requests.get(url, params=params)

        response.status = f'{result.status_code} {result.reason}'
        response.content_type = result.headers['content-type']
        response.body = result.text
