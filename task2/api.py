from flask import Blueprint, abort, jsonify, request
from .task import solve_task


task2_api = Blueprint('task2', __name__)


@task2_api.route('/input', methods=['POST'])
def task1():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    try:
        result = solve_task(_input)
    except:
        abort(400, {})

    return jsonify(dict(
        result=result,
    ))
