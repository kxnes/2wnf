#!/usr/bin/env python3

import argparse
import importlib

import tornado.ioloop

from config import FRAMEWORKS


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--framework', required=True, choices=FRAMEWORKS)
    parser.add_argument('-a', '--application', default='app')
    args = parser.parse_args()

    framework = importlib.import_module(f'frameworks.fw_{args.framework}')
    if args.framework == 'aiohttp' and args.application != 'app':
        raise AttributeError('For `aiohttp` dev server use `app` application name.')

    # `cherrypy` don't want `app` instance (had internal)
    application = getattr(framework, args.application) if args.framework not in ('cherrypy', 'django') else None

    FRAMEWORKS[args.framework](application)

    # `tornado` runs only if `IOLoop` present
    if args.framework == 'tornado':
        tornado.ioloop.IOLoop.current().start()
