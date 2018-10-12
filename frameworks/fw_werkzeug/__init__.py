import werkzeug.wrappers

from config import PING_MESSAGE


# noinspection PyUnusedLocal
@werkzeug.wrappers.Request.application
def app(request):
    return werkzeug.wrappers.Response(PING_MESSAGE.format(app='werkzeug'))
