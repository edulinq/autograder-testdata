#!/usr/bin/env python3

"""
Generate test data using the LMS Toolkit.
"""

import argparse
import os
import sys

import autograder.testing.testdata

THIS_DIR: str = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
ROOT_DIR: str = os.path.join(THIS_DIR, '..')
TEST_DATA_DIR: str = os.path.join(ROOT_DIR, 'testdata', 'http')

DEFAULT_SOURCE_DIR: str = os.path.join(ROOT_DIR, 'autograder-server')
DEFAULT_PORT: int = 8080

def run_cli(args):
    config = {
        'server': f"127.0.0.1:{args.port}",
        'server_start_command': f"go run cmd/server/main.go --unit-testing --log-level DEBUG --config web.port={args.port}",
        'server_stop_command': "pkill -f 'main --unit-testing --log-level DEBUG'",
        'http_exchanges_out_dir': args.out_dir,
        'fail_fast': args.fail_fast,
        'pattern': args.pattern,
    }

    os.chdir(args.source_dir)

    return autograder.testing.testdata.generate(config)

def main():
    return run_cli(_get_parser().parse_args())

def _get_parser():
    parser = argparse.ArgumentParser(description = __doc__.strip())

    parser.add_argument('--source-dir', dest = 'source_dir',
        action = 'store', type = str, default = DEFAULT_SOURCE_DIR,
        help = 'The source directory to build and run the autograder server from (default: %(default)s).')

    parser.add_argument('--port', dest = 'port',
        action = 'store', type = int, default = DEFAULT_PORT,
        help = 'The port to use for the server (default: %(default)s).')

    parser.add_argument('--out-dir', dest = 'out_dir',
        action = 'store', type = str, default = TEST_DATA_DIR,
        help = 'Where the output HTTP exchanges will be written (default: %(default)s).')

    parser.add_argument('--fail-fast', dest = 'fail_fast',
        action = 'store_true', default = False,
        help = 'If true, stop on the first test failure (default: %(default)s).')

    parser.add_argument('--pattern', dest = 'pattern',
        action = 'store', type = str, default = None,
        help = 'If provided, only run tests that match this mattern.')

    return parser

if (__name__ == '__main__'):
    sys.exit(main())
