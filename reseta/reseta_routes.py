from flask import Blueprint, jsonify
from .reseta_model import resetArrays

reset_blueprint = Blueprint('reset', __name__)

@reset_blueprint.route("/reseta", methods = ["POST"])
def reset_dados():
    resetArrays()
    return jsonify({'Success': True})