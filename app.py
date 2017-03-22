from flask import Flask, abort, jsonify, request

app = Flask(__name__)


@app.route('/task1/input', methods=['POST'])
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
