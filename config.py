import os
import asyncio
import logging
import pathlib
import uvicorn
import cherrypy

from aiohttp_devtools.cli import runserver as aioserver
# noinspection PyProtectedMember
from cherrypy import server
from django.core.management.commands import runserver as djserver
from tornado.httpserver import HTTPServer
from twisted.internet import reactor, endpoints
from uvicorn.reloaders.statreload import StatReload
from werkzeug.serving import run_simple
from hypercorn import run, Config

# == Settings == #

PROJECT_ROOT = pathlib.Path(__file__).parent

FRAMEWORKS_ROOT = PROJECT_ROOT / 'frameworks'

HOST = '127.0.0.1'

PORT = 8000

DEBUG = True

RELOAD = True

PING_MESSAGE = '{app} is ready!'

FRAMEWORKS = {
    'aiohttp':
        lambda app: aioserver([
            f'{AIOHTTP_DEV_CLIENT}',
            '--host', HOST,
            '--port', PORT,
            '--debug-toolbar' if DEBUG else '--no-debug-toolbar',
            '--livereload' if RELOAD else '--no-livereload'
        ]),
    'bottle':
        lambda app: app.run(host=HOST, port=PORT, debug=DEBUG, reloader=RELOAD),
    'cherrypy':
        lambda app: cherrypy.server.start(),
    'django':
        lambda app: djserver.Command().handle(
            addrport=f'{HOST}:{PORT}', use_reloader=RELOAD, use_threading=True, use_ipv6=False
        ),
    'falcon':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOAD),
    'flask':
        lambda app: app.run(HOST, PORT, debug=DEBUG, use_reloader=RELOAD),
    'hypercorn':
        lambda app: run.run_single(app, Config.from_mapping(
            {'host': HOST, 'port': PORT, 'debug': DEBUG, 'use_reloader': RELOAD}
        ), loop=asyncio.get_event_loop()),
    'molten':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOAD),
    'pyramid':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOAD),
    'quart':
        lambda app: app.run(HOST, PORT, debug=DEBUG, use_reloader=RELOAD, loop=asyncio.get_event_loop()),
    'sanic':
        lambda app: app.run(HOST, PORT, debug=DEBUG, auto_reload=RELOAD),
    'starlette':
        lambda app: StatReload(logging.getLogger(__name__)).run(
            uvicorn.run, {'app': app, 'host': HOST, 'port': PORT, 'debug': DEBUG}
        ) if RELOAD else uvicorn.run(app, HOST, PORT, debug=DEBUG),
    'tornado':
        lambda app: HTTPServer(app).listen(PORT, HOST),
    'turbogears':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOAD),
    'twisted':
        lambda app: endpoints.serverFromString(reactor, f'tcp:{PORT}:interface={HOST}').listen(app),
    'uvicorn':
        lambda app: StatReload(logging.getLogger(__name__)).run(
            uvicorn.run, {'app': app, 'host': HOST, 'port': PORT, 'debug': DEBUG}
        ) if RELOAD else uvicorn.run(app, HOST, PORT, debug=DEBUG),
    'vibora':
        lambda app: app.run(HOST, PORT, debug=DEBUG),
    'weppy':
        lambda app: app.run(HOST, PORT, debug=DEBUG, reloader=RELOAD),
    'werkzeug':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOAD),
    'wheezyweb':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOAD)
}


# == WORKAROUND == #

# for `flask` development serving without warnings
os.environ.setdefault('FLASK_ENV', 'development')
# for `aiohttp` run server client
AIOHTTP_DEV_CLIENT = (FRAMEWORKS_ROOT / 'fw_aiohttp' / '__init__.py').as_posix()
# for `cherrypy` serving on properly address
server.bind_addr = (HOST, PORT)
