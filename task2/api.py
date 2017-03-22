from flask import Blueprint, abort, jsonify, request


task2_api = Blueprint('task2', __name__)


@task2_api.route('/input', methods=['POST'])
def task1():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    # TODO processing

    return jsonify(dict(
        result=[],
    ))
