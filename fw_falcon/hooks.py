import falcon


def max_body(limit):

    def hook(request, response, resource, params):
        print('request:', request)
        print('response:', response)
        print('resource:', resource)
        print('params:', params)
        length = request.content_length
        if length is not None and length > limit:
            raise falcon.HTTPRequestEntityTooLarge('Request body is too large', 'The size of the request is too large.')

    return hook
