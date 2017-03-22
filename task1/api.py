from flask import Blueprint, abort, jsonify, request


task1_api = Blueprint('task1', __name__)


@task1_api.route('/input', methods=['POST'])
def task1():
    _input = request.get_json(force=True)

    if not _input:
        abort(400)

    # TODO processing

    return jsonify(dict(
        feasible=True,
        totalCost=15,
        depotId=3,
        recommendedOffers=[],
    ))
