#!/usr/bin/env python3

import argparse
import importlib

from config import FRAMEWORKS


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--framework', required=True, choices=FRAMEWORKS)
    parser.add_argument('-a', '--application', default='app')
    args = parser.parse_args()

    framework = importlib.import_module(f'fw_{args.framework}')
    if args.framework == 'aiohttp' and args.application != 'app':
        raise AttributeError('For `aiohttp` dev server use `app` application name.')

    application = getattr(framework, args.application) if args.framework != 'cherrypy' else None

    FRAMEWORKS[args.framework](application)
