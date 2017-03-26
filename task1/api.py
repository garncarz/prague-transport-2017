import logging

from flask import Blueprint, abort, jsonify, request


logger = logging.getLogger(__name__)

task1_api = Blueprint('task1', __name__)


@task1_api.route('/input', methods=['POST'])
def task1():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    logger.info('Task1: input', extra={'data': {'input': _input}})

    # TODO processing

    _output = dict(
        feasible=True,
        totalCost=15,
        depotId=3,
        recommendedOffers=[],
    )

    logger.info('Task1: output', extra={'data': {'output': _output}})

    return jsonify(_output)
