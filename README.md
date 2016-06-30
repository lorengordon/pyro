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

To run the all tests run:

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
