import os
import sys
import asyncio
import logging
import pathlib
import uvicorn

from uvicorn.reloaders.statreload import StatReload
from werkzeug.serving import run_simple


PROJECT_ROOT = pathlib.Path(__file__).parent

SRC_ROOT = PROJECT_ROOT / 'src'

HOST = '127.0.0.1'

PORT = 8000

DEBUG = True

RELOADER = True

PING_MESSAGE = '{app} is ready!'

FRAMEWORKS = {
    'falcon':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOADER),
    'quart':
        lambda app: app.run(HOST, PORT, debug=DEBUG, use_reloader=RELOADER, loop=asyncio.get_event_loop()),
    'sanic':
        lambda app: app.run(HOST, PORT, debug=DEBUG, auto_reload=RELOADER),
    'starlette':
        lambda app: StatReload(logging.getLogger(__name__)).run(
            uvicorn.run, {'app': app, 'host': HOST, 'port': PORT, 'debug': DEBUG}
        ) if RELOADER else uvicorn.run(app, HOST, PORT, debug=DEBUG),
    'weppy':
        lambda app: app.run(HOST, PORT, debug=DEBUG, reloader=RELOADER),
    'molten':
        lambda app: run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOADER),
    'flask':
        lambda app: app.run(HOST, PORT, debug=DEBUG, use_reloader=RELOADER),
    'bottle':
        lambda app: app.run(host=HOST, port=PORT, debug=DEBUG, reloader=RELOADER)
}


# for `flask` development serving without warnings
os.environ.setdefault('FLASK_ENV', 'development')
# for resolve fw_{__name__} without `src` by name
sys.path.append(SRC_ROOT.as_posix())
