from flask import Blueprint, jsonify, request
from .aluno_model import addStudent, getStudents, getStudentById, attStudent, deleteStudent
from errors import EmptyStringError, IdNotExist

aluno_blueprint = Blueprint('aluno', __name__)

@aluno_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    try:
        addStudent(data)
        return jsonify(data), 201
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'}), 400
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'}), 400
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404
    
@aluno_blueprint.route("/alunos", methods = ['GET'])
def get_alunos():
    return jsonify(getStudents())

@aluno_blueprint.route("/alunos/<id>", methods = ['GET'])
def get_aluno(id):
    try:
        return jsonify(getStudentById(id))
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404

@aluno_blueprint.route("/alunos/<id>", methods = ['PUT'])
def update_aluno(id):
    data = request.json
    try:
        attStudent(id, data)
        return jsonify(getStudentById(id))
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'}), 400
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'}), 400
    

@aluno_blueprint.route("/alunos/<id>", methods = ['DELETE'])
def delete_aluno(id):
    try:
        deleteStudent(id)
        return jsonify({'Success': True})
    except IdNotExist as e:
        return jsonify({'Error': e.message}), 404