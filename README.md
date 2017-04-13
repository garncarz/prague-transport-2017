# Next stop: Montréal

[![Build Status](https://travis-ci.org/mgp4/prague-transport-2017.svg?branch=master)](https://travis-ci.org/mgp4/prague-transport-2017)

This is our solution for [Prague Hackathon 2017](https://praguehackathon.com).
See the attached [task assignment](task_assignment.md).


## Installation

Needed:
- Python 3
- Redis
- Supervisord
- gcc >= 4.8.1, boost >= 1.34, make

Preferably under `virtualenv` (`virtualenv venv; source venv/bin/activate`):

`pip install pip-tools` (once)

`pip-sync requirements*.txt` (keeping the PyPI dependencies up-to-date)

`cd task1 && make` to compile the Task 1 solver.


## Configuration

Customized settings are expected in `main/settings_local.py`.
(But they shouldn't be needed, just Sentry DSN, if you want to log to Sentry.)


## Usage

`supervisord` starts Supervisord with background services.
They can be controlled by `supervisorctl` then.
Logs are stored in the `log` directory.


## Architecture

There are several services managed by Supervisord:
- uWSGI Flask application –
    processing REST API requests by pushing them to the Redis queue,
    and responding after they're computed;
- Redis server – message queue between the main application and workers,
    also used for caching;
- Celery workers – computing solutions, if they're not already cached.

Caching is used to ensure that long-running computation is not interrupted.
E.g. when request timeout is reached, the next time the same request arrives,
the cached result is returned immediately.


## Development

`./app.sh` runs the Flask application.

`./test.sh` runs pytest suite.

`./real_tests.py` checks responses from the production server,
based on JSON files in the `real_tests` directory.


## Task 1

The problem is solved with using of Tarjan's implementation of Edmond's algorithm
(http://edmonds-alg.sourceforge.net/) in C++ language. Since the implementation
is intented to be used on dense graph, non-existing edges will get maximum possible
weight to be cut at the beginning of the run. The worst time complexity of this
algorithm is quadratic due to number of vertices.


## Task 2

There is basic decission tree from scikit-learn used to categorize airplanes based
on measured noise level, brake distance and vibration.
