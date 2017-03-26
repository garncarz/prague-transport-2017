import json

from deepdiff import DeepDiff
import pytest

from main.app import app
from main import settings
from task1 import task


with open('tests/task1_input.json') as f:
    _input = json.loads(f.read())

with open('tests/task1_output.json') as f:
    _output = json.loads(f.read())


@pytest.mark.skipif(not settings.TESTING_API,
                    reason='At least one Celery worker needed to test API.')
def test_api():
    response = app.test_client().post('/task1/input', data=json.dumps(_input))
    data = json.loads(response.data.decode())

    assert data['feasible'] == True
    assert data['totalCost'] == 15


def test_task():
    result = task._solve(_input)
    assert not DeepDiff(result, _output, ignore_order=True)


def test_dict_to_stdin():
    result = task.dict_to_stdin(_input)
    assert result.decode() == '''\
4
0 1 6
1 2 10
2 1 10
1 3 12
3 2 8
3 0 1
'''


def test_stdout_to_dict():
    b = '''\
1 15 3
0 1 6
3 0 1
3 2 8
'''.encode()
    result = task.stdout_to_dict(b)
    assert result == _output
