#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

try:
    import pypandoc
    # Strip Markdown image tags from README.md and convert to rst
    long_description = '%s\n%s' % (
        re.compile('^\[!\[.*$', re.M).sub('', read('README.md')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.md'))
    )
    long_description = pypandoc.convert(
        long_description.lstrip('\n'),
        'rst',
        format='md')
    long_description = long_description.replace('\r\n', '\n')
except (ImportError, OSError):
    # pandoc is not installed, fallback to using raw contents
    print("WARNING: Pandoc not found. Long_description conversion failure. "
          "Do not upload this package to pypi.")
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup(
    name='pyro',
    version='0.1.0',
    license="Apache Software License 2.0",
    description='An example package. Generated with cookiecutter-pyro.',
    long_description=long_description,
    author='Maintainers of Pyro',
    author_email='projects@plus3it.com',
    url='https://github.com/lorengordon/pyro',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        'click>=6.0',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    entry_points={
        'console_scripts': [
            'pyro = pyro.cli:main',
        ]
    },
)
