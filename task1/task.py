import re
import subprocess

from main import cache, celery


def dict_to_stdin(d):
    s = '%d\n' % d['citiesCount']
    for offer in d['costOffers']:
        s += '%d %d %d\n' % (offer['from'], offer['to'], offer['price'])
    return s.encode()


def stdout_to_dict(b):
    d = {}
    m = re.split(r'[ \t\n\r:]+', b.decode())

    d['feasible'] = True if m[0] == '1' else False
    d['totalCost'] = int(m[1])
    d['depotId'] = int(m[2])

    d['recommendedOffers'] = []
    for i in range(3, len(m) - 1, 3):
        d['recommendedOffers'].append({
            'from': int(m[i]),
            'to': int(m[i + 1]),
            'price': int(m[i + 2]),
        })

    return d


def _solve(_input):
    p = subprocess.Popen(['task1/find_hub'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    p.stdin.write(dict_to_stdin(_input))
    p.stdin.close()
    p.wait()
    return stdout_to_dict(p.stdout.read())


@celery.app.task
def solve(_input):
    key = {'task': 1, 'input': _input}
    result = cache.get(key)
    if not result:
        result = _solve(_input)
        cache.set(key, result)
    return result
