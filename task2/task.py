from sklearn import tree

clf = tree.DecisionTreeClassifier()

def prepare_classifier(data):
    target = []
    _input = []
    for a in data:
        target.append(a['type'])
        _input.append((a['noise-level'], a['brake-distance'], a['vibrations']))
    clf.fit(_input, target)


def predict(data):
    result = []
    for a in data:
        _input = ((a['noise-level'], a['brake-distance'], a['vibrations']))
        cls = clf.predict(_input)[0]
        result.append({'id': a['id'], 'type': cls})
    return result


def solve_task(data):
    try:
        learning_set = data['measurements']
        testing_set = data['samples']
    except IndexError:
        return None # or raise some custom excpetion?
    prepare_classifier(learning_set)
    response = predict(testing_set)
    return response
