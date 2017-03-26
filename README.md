# Next stop: Montréal

[![Build Status](https://travis-ci.org/mgp4/prague-transport-2017.svg?branch=master)](https://travis-ci.org/mgp4/prague-transport-2017)


## Installation

Needed:
- Python 3
- Redis
- Supervisord

Preferably under `virtualenv` (`virtualenv venv; source venv/bin/activate`):

`pip install pip-tools` (once)

`pip-sync requirements*.txt` (keeping the PyPI dependencies up-to-date)


## Usage

`./app.sh`


## Testing

`./test.sh`

## Task 1

### Design and implementation

The problem is solved with using of Tarjan's implementation of Edmond's algorithm
(http://edmonds-alg.sourceforge.net/) in C++ language. Since the implementation
is intented to be used on dense graph, non-existing edges will get maximum possible
weight to be cut at the beginning of the run. The worst time complexity of this
algorithm is quadratic due to number of vertices.

### Requirements and installation

`gcc >= 4.8.1`, `boost >= 1.34` and `make`. A standard Makefile is provided.
