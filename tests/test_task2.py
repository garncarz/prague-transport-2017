import json

from app import app


def test_task2():
    _input = {
        'measurements': [
            {
                'type': 'A380',
                'noise-level': 103,
                'brake-distance': 2130,
                'vibrations': 0.81
            },
            {
                'type': 'A380',
                'noise-level': 101,
                'brake-distance': 2070,
                'vibrations': 0.88
            },
            {
                'type': '737',
                'noise-level': 94,
                'brake-distance': 1730,
                'vibrations': 0.82
            },
            {
                'type': '737',
                'noise-level': 96,
                'brake-distance': 1820,
                'vibrations': 0.79
            }
        ],
        'samples' : [
            {
                'id': 1,
                'noise-level': 102,
                'brake-distance': 2105,
                'vibrations': 0.80
            },
            {
                'id': 2,
                'noise-level': 97,
                'brake-distance': 1830,
                'vibrations': 0.80
            },
        ],
    }

    response = app.test_client().post('/task2/input', data=json.dumps(_input))
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert 'result' in data
    assert len(data['result']) == 2
    # TODO more asserts
