import json
import falcon


class AuthMiddleware:
    def process_request(self, request, response):
        print('request:', request)
        print('response:', response)
        token = request.get_header('Authorization')
        account_id = request.get_header('Account-ID')

        challenges = ['Token type="Fernet"']

        if token is None:
            raise falcon.HTTPUnauthorized(
                'Auth token required', 'Please provide an auth token.', challenges
            )

        if not self._token_is_valid(token, account_id):
            raise falcon.HTTPUnauthorized(
                'Authentication required', 'The provided auth token is not valid.', challenges
            )

    @staticmethod
    def _token_is_valid(token, account_id):
        print('token:', token)
        print('account_id:', account_id)
        return True


# noinspection PyMethodMayBeStatic
class RequireJSONMiddleware:
    def process_request(self, request, response):
        print('request:', request)
        print('response:', response)
        if not request.client_accepts_json:
            raise falcon.HTTPNotAcceptable('This API only supports responses encoded as JSON.')

        if request.method in ('POST', 'PUT'):
            if 'application/json' not in request.content_type:
                raise falcon.HTTPUnsupportedMediaType('This API only supports requests encoded as JSON.')


# noinspection PyMethodMayBeStatic
class JSONTranslatorMiddleware:
    def process_request(self, request, response):
        print('request:', request)
        print('response:', response)
        if request.content_length in (None, 0):
            return

        body = request.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body', 'A valid JSON document is required.')

        try:
            request.context['doc'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON', 'Could not decode the request body.')

    def process_response(self, request, response, resource):
        print('request:', request)
        print('response:', response)
        print('resource:', resource)
        if 'result' not in response.context:
            return

        response.body = json.dumps(response.context['result'])
