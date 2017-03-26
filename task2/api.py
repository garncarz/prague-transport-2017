import logging

from flask import Blueprint, abort, jsonify, request
from . import task


logger = logging.getLogger(__name__)

task2_api = Blueprint('task2', __name__)


@task2_api.route('/input', methods=['POST'])
def task2():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    logger.info('Task2: input', extra={'data': _input})

    try:
        job = task.solve.apply_async(args=[_input])
        result = job.get()
    except Exception:
        logger.exception('Task2: error solving')
        abort(400)

    _output = dict(
        result=result,
    )

    logger.info('Task2: output', extra={'data': _output})

    return jsonify(_output)
