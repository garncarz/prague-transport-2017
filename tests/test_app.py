import json

from app import app


def test_task1():
    _input = {
        'citiesCount' : 4,
        'costOffers' : [
            {
                'from' : 0,
                'to' : 1,
                'price' : 6
            },
            {
                'from' : 1,
                'to' : 2,
                'price' : 10
            },
            {
                'from' : 2,
                'to' : 1,
                'price' : 10
            },
            {
                'from' : 1,
                'to' : 3,
                'price' : 12
            },
            {
                'from' : 3,
                'to' : 2,
                'price' : 8
            },
            {
                'from' : 3,
                'to' : 0,
                'price' : 1
            },
        ],
    }

    response = app.test_client().post('/task1/input', data=json.dumps(_input))
    data = json.loads(response.data)

    assert data['feasible'] == True
    assert data['totalCost'] == 15
