import json

import pytest

from main.app import app
from main import settings
from task2 import task


with open('tests/task2.json') as f:
    _input = json.loads(f.read())


@pytest.mark.skipif(not settings.TESTING_API,
                    reason='At least one Celery worker needed to test API.')
def test_api():
    response = app.test_client().post('/task2/input', data=json.dumps(_input))
    assert response.status_code == 200

    data = json.loads(response.data.decode())
    assert 'result' in data
    assert len(data['result']) == len(_input['samples'])
    for s in _input['samples']:
        assert any(d['id'] == s['id'] for d in data['result'])


def test_task():
    result = task._solve(_input)
    assert result == [
        {
            'id' : 1,
            'type' : 'A380',
        },
        {
            'id' : 2,
            'type' : '737',
        },
    ]
