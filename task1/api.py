import logging

from flask import Blueprint, abort, jsonify, request
from . import task


logger = logging.getLogger(__name__)

task1_api = Blueprint('task1', __name__)


@task1_api.route('/input', methods=['POST'])
def task1():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    logger.info('Task1: input', extra={'data': {'input': _input}})

    try:
        job = task.solve.apply_async(args=[_input])
        result = job.get()
    except Exception:
        logger.exception('Task1: error solving')
        abort(400)

    _output = result
    logger.info('Task1: output', extra={'data': {'output': _output}})

    return jsonify(_output)
