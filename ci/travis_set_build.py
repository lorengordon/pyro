#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update the version string with a build number"""

from __future__ import absolute_import
from __future__ import print_function

import io
import os
import re


PROJECT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.pardir)
)
BUILD_NUMBER = os.environ.get('TRAVIS_BUILD_NUMBER', '')
VERSION_FILE_PATHS = ('src', 'pyro', '__init__.py')


def replace(file_path, pattern, repl, flags=0):
    with io.open(file_path, mode="r+") as fh_:
        file_contents = fh_.read()
        file_contents = re.sub(pattern, repl, file_contents)
        fh_.seek(0)
        fh_.truncate()
        fh_.write(file_contents)


def main(args):
    build = args.build
    file_paths = args.file_paths
    # The version line must have the form
    # __version__ = 'ver'
    pattern = r"^(__version__ = ['\"])([^'\"]*)(['\"])"
    repl = r"\g<1>\g<2>.dev{0}\g<3>".format(build)
    version_file = os.path.join(PROJECT_DIR, *file_paths)
    print(
        'Updating version in version_file "{0}" with build "{1}"'
        .format(version_file, build)
    )
    replace(version_file, pattern, repl, flags=re.M)


if '__main__' == __name__:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--build',
        default=BUILD_NUMBER,
        help='Build number to set (default: {0})'.format(BUILD_NUMBER)
    )
    parser.add_argument(
        '--file-paths',
        default=VERSION_FILE_PATHS,
        help=(
            'Tuple of paths relative to the project root to a file containing '
            'the version string (default: {0})'.format(VERSION_FILE_PATHS)
        )
    )

    args = parser.parse_args()
    main(args)
