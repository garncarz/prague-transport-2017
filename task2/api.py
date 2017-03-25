import logging

from flask import Blueprint, abort, jsonify, request


logger = logging.getLogger(__name__)

task2_api = Blueprint('task2', __name__)


@task2_api.route('/input', methods=['POST'])
def task2():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    logger.info('Task2: input', extra={'data': _input})

    # TODO processing

    _output = dict(
        result=[],
    )

    logger.info('Task2: output', extra={'data': _output})

    return jsonify(_output)
