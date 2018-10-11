import sys
import asyncio
import pathlib
import uvicorn
import werkzeug.serving


PROJECT_ROOT = pathlib.Path(__file__).parent

SRC_ROOT = PROJECT_ROOT / 'src'

HOST = '127.0.0.1'

PORT = 8000

DEBUG = True

RELOADER = True

PING_MESSAGE = '{app} is ready!'

FRAMEWORKS = {
    'falcon': lambda app: werkzeug.serving.run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOADER),
    'quart': lambda app: app.run(HOST, PORT, debug=DEBUG, use_reloader=RELOADER, loop=asyncio.get_event_loop()),
    'sanic': lambda app: app.run(HOST, PORT, debug=DEBUG, auto_reload=RELOADER),
    'starlette': lambda app: uvicorn.run(app, HOST, PORT, debug=DEBUG),
    'weppy': lambda app: app.run(HOST, PORT, debug=DEBUG, reloader=RELOADER),
    'molten': lambda app: werkzeug.serving.run_simple(HOST, PORT, app, use_debugger=DEBUG, use_reloader=RELOADER),
}


# for resolve fw_{__name__} without `src` by name
sys.path.append(SRC_ROOT.as_posix())
