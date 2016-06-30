[![Documentation Status](https://readthedocs.org/projects/pyro/badge/?style=flat)](https://readthedocs.org/projects/pyro)
[![Travis-CI Build Status](https://travis-ci.org/lorengordon/pyro.svg?branch=master)](https://travis-ci.org/lorengordon/pyro)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/lorengordon/pyro?branch=master&svg=true)](https://ci.appveyor.com/project/lorengordon/pyro)
[![Requirements Status](https://requires.io/github/lorengordon/pyro/requirements.svg?branch=master)](https://requires.io/github/lorengordon/pyro/requirements/?branch=master)
[![Coverage Status](https://codecov.io/github/lorengordon/pyro/coverage.svg?branch=master)](https://codecov.io/github/lorengordon/pyro)
[![Code Quality Status](https://landscape.io/github/lorengordon/pyro/master/landscape.svg?style=flat)](https://landscape.io/github/lorengordon/pyro/master)
[![PyPI Package Latest Release](https://img.shields.io/pypi/v/pyro.svg?style=flat)](https://pypi.python.org/pypi/pyro)
[![PyPI Package monthly downloads](https://img.shields.io/pypi/dm/pyro.svg?style=flat)](https://pypi.python.org/pypi/pyro)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/pyro.svg?style=flat)](https://pypi.python.org/pypi/pyro)
[![PyPI Supported versions](https://img.shields.io/pypi/pyversions/pyro.svg?style=flat)](https://pypi.python.org/pypi/pyro)
[![PyPI Supported implementations](https://img.shields.io/pypi/implementation/pyro.svg?style=flat)](https://pypi.python.org/pypi/pyro)

# Pyro

## Overview

An example package. Generated with cookiecutter-pyro.

*   Free software: Apache Software License 2.0

## Installation

```bash
pip install pyro
```

## Documentation

<https://pyro.readthedocs.io/>

## Development

To run the all tests run::

```bash
tox
```

Note, to combine the coverage data from all the tox environments run:

*   Windows

```bash
set PYTEST_ADDOPTS=--cov-append
tox
```

*   Other

```bash
PYTEST_ADDOPTS=--cov-append tox
```
