from flask import Blueprint, jsonify, request
from .professor_model import addProfessor, getProfessors, getProfessorById, updateProfessor, deleteProfessor
from errors import EmptyStringError, IdNotExist

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    try:
        addProfessor(data)
        return jsonify(data), 201
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias.'}), 400
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave.'}), 400

@professor_blueprint.route("/professores", methods=['GET'])
def get_professors():
    return jsonify(getProfessors())

@professor_blueprint.route("/professores/<int:id>", methods=['GET'])
def get_professor(id):
    try:
        return jsonify(getProfessorById(id))
    except IdNotExist as e:
        return jsonify({'Error': str(e)}), 404

@professor_blueprint.route("/professores/<int:id>", methods=['PUT'])
def update_professor(id):
    data = request.json
    try:
        updateProfessor(id, data)
        return jsonify(getProfessorById(id))
    except IdNotExist as e:
        return jsonify({'Error': str(e)}), 404
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias.'}), 400
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave.'}), 400

@professor_blueprint.route("/professores/<int:id>", methods=['DELETE'])
def delete_professor(id):
    try:
        deleteProfessor(id)
        return jsonify({'Success': True})
    except IdNotExist as e:
        return jsonify({'Error': str(e)}), 404