import argparse
import importlib

from config import FRAMEWORKS


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--framework', required=True, choices=FRAMEWORKS)
    parser.add_argument('-a', '--application', default='app')
    args = parser.parse_args()
    FRAMEWORKS[args.framework](getattr(importlib.import_module(f'fw_{args.framework}'), args.application))
