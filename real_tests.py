#!/usr/bin/env python3

import json
import os

from deepdiff import DeepDiff
import requests


REAL_URL = 'http://trans.garncarz.cz/task%s/input'


def main():
    for task in os.listdir('real_tests'):
        task_dir = 'real_tests/%s' % task
        task_url = REAL_URL % task

        for test in os.listdir(task_dir):
            test_dir = '%s/%s' % (task_dir, test)

            with open('%s/input.json' % test_dir) as f:
                _input = f.read()
            with open('%s/output.json' % test_dir) as f:
                expected = json.loads(f.read())

            resp = requests.post(task_url, data=_input)
            data = json.loads(resp.text)

            diff = DeepDiff(data, expected, ignore_order=True)
            if diff:
                print('ERROR %s/%s' % (task, test))
                print(diff)


if __name__ == '__main__':
    main()
