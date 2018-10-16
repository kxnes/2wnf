#!/usr/bin/env python3

import argparse
import importlib

import tornado.ioloop
import twisted.internet.reactor
from pulsar.apps.wsgi import WSGIServer

from config import FRAMEWORKS, HOST, PORT, DEBUG, RELOAD


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--framework', default='kekos', choices=FRAMEWORKS)
    parser.add_argument('-a', '--application', default='app')
    args = parser.parse_args()

    framework = importlib.import_module(f'frameworks.fw_{args.framework}')
    if args.framework == 'aiohttp' and args.application != 'app':
        raise AttributeError('For `aiohttp` dev server use `app` application name.')

    # `cherrypy`, `django` don't want `app` instance (has internal)
    application = getattr(framework, args.application) if args.framework not in ('cherrypy', 'django') else None

    # `tornado` runs only if `IOLoop` present
    if args.framework == 'tornado':
        tornado.ioloop.IOLoop.current().start()

    # `twisted` runs from internal reactor
    if args.framework == 'twisted':
        # noinspection PyUnresolvedReferences
        twisted.internet.reactor.run()  # some BLACK MAGIC here

    # `pulsar` runs throw `hardcode`
    if args.framework == 'kekos':
        delattr(args, 'framework')
        print(args.framework)
        WSGIServer(callable=application, bind=f'{HOST}:{PORT}', debug=DEBUG, reload=RELOAD).start()
    # else:
    #     FRAMEWORKS[args.framework](application)
