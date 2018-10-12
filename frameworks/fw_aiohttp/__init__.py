import aiohttp.web

from config import PING_MESSAGE


# noinspection PyUnusedLocal
async def ping(request):
    return aiohttp.web.Response(text=PING_MESSAGE.format(app='aiohttp'))


app = aiohttp.web.Application()
app.add_routes([
    aiohttp.web.get('/', ping)
])
