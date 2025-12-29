#!/usr/bin/env python3

"""
Verify test data using a local source directory.
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
        'test_data_dir': args.test_data_dir,
        'fail_fast': args.fail_fast,
    }

    os.chdir(args.source_dir)

    return autograder.testing.testdata.verify(config)

def main():
    return run_cli(_get_parser().parse_args())

def _get_parser():
    parser = argparse.ArgumentParser(description = __doc__.strip())

    parser.add_argument('--test-data-dir', dest = 'test_data_dir',
        action = 'store', type = str, default = TEST_DATA_DIR,
        help = 'The directory with test data to verify (default: %(default)s).')

    parser.add_argument('--source-dir', dest = 'source_dir',
        action = 'store', type = str, default = DEFAULT_SOURCE_DIR,
        help = 'The source directory to build and run the autograder server from (default: %(default)s).')

    parser.add_argument('--port', dest = 'port',
        action = 'store', type = int, default = DEFAULT_PORT,
        help = 'The port to use for the server (default: %(default)s).')

    parser.add_argument('--fail-fast', dest = 'fail_fast',
        action = 'store_true', default = False,
        help = 'If true, stop on the first test failure (default: %(default)s).')

    return parser

if (__name__ == '__main__'):
    sys.exit(main())
