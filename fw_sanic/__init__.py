from sanic import Sanic, response


app = Sanic(strict_slashes=True)


# noinspection PyUnusedLocal
@app.route('/hw/')
async def hello_world(request):
    return response.text('Hello, world!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
