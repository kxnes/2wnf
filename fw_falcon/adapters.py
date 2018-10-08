import requests


class SinkAdapter(object):

    engines = {
        'google': 'https://www.google.com/',
        'yandex': 'https://www.yandex.ru/'
    }

    def __call__(self, req, resp, engine):
        url = self.engines[engine]
        params = {'q': req.get_param('q', True)}
        result = requests.get(url, params=params)

        resp.status = str(result.status_code) + ' ' + result.reason
        resp.content_type = result.headers['content-type']
        resp.body = result.text
