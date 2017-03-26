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
