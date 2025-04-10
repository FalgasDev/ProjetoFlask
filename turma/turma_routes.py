from flask import Blueprint, jsonify, request
from .turma_model import addClass, getClasses, getClassById, attClass, deleteClass
from errors import EmptyStringError, IdNotExist

turma_blueprint = Blueprint('turma', __name__)

@turma_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    try:
        addClass(data)
        return jsonify(data), 201
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'}), 400
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'}), 400
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404
    
@turma_blueprint.route("/turmas", methods = ['GET'])
def get_turmas():
    return jsonify(getClasses())

@turma_blueprint.route("/turmas/<id>", methods = ['GET'])
def get_turma(id):
    try:
        return jsonify(getClassById(id)) 
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404

@turma_blueprint.route("/turmas/<id>", methods = ['PUT'])
def update_turma(id):
    data = request.json
    try:
        attClass(id, data)
        return(getClassById(id))
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'}), 400
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'}), 400
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404

@turma_blueprint.route("/turmas/<id>", methods = ['DELETE'])
def delete_turma(id):
    try:
        deleteClass(id)
        return jsonify({'Success': True})
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404