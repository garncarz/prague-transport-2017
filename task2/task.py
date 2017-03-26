from sklearn import tree

from main import celery


def prepare_classifier(clf, data):
    target = []
    _input = []
    for a in data:
        target.append(a['type'])
        _input.append((a['noise-level'], a['brake-distance'], a['vibrations']))
    clf.fit(_input, target)


def predict(clf, data):
    result = []
    for a in data:
        _input = [(a['noise-level'], a['brake-distance'], a['vibrations'])]
        cls = clf.predict(_input)[0]
        result.append({'id': a['id'], 'type': cls})
    return result


def _solve(data):
    try:
        learning_set = data['measurements']
        testing_set = data['samples']
    except IndexError:
        return None # or raise some custom excpetion?
    clf = tree.DecisionTreeClassifier()
    prepare_classifier(clf, learning_set)
    response = predict(clf, testing_set)
    return response


@celery.app.task
def solve(_input):
    return _solve(_input)
