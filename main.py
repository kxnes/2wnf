#!/usr/bin/env python3

import argparse
import importlib

import tornado.ioloop
import twisted.internet.reactor

from config import FRAMEWORKS


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_subparsers()
    parser.add_argument('-f', '--framework', required=True, choices=FRAMEWORKS)
    parser.add_argument('-a', '--application', default='app')
    args = parser.parse_args(namespace=argparse.Namespace())

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

    FRAMEWORKS[args.framework](application)
