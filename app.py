from flask import Flask, jsonify, request
from errors import EmptyStringError, IdNotExist

app = Flask(__name__)
professores = []
alunos = []
turmas = []
professores_deletados = []
alunos_deletados = []
turmas_deletadas = []

# ---- Rota Post Professores ---- #
@app.route('/professores', methods = ['POST'])
def addProfessor():
    data = request.json
    try:
        if 'name' and 'age' and 'subject' and 'info' not in data:
            raise KeyError
        
        if data['name'] == "" or data['age'] == "" or data['subject'] == "" or data['info'] == "":
            raise EmptyStringError

        professores.append({
            "name": data['name'], 
            "id": len(professores) + len(professores_deletados) + 1, 
            "age": data['age'], 
            "subject": data['subject'], 
            "info": data['info']
            })
        
        return jsonify({'success': True})

    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'})
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'})

# ---- Rota Get Professores ---- #
@app.route("/professores", methods = ['GET'])
def getProfessors():
    data = professores
    return jsonify(data)

# ---- Rota Get Professor Por ID ---- #
@app.route("/professores/<id>", methods = ['GET'])
def getProfessorById(id):
    data = {}
    idExiste = False
    try:
        for professor in professores:
            if professor['id'] == int(id):
                data = professor
                idExiste = True
                break
        
        if idExiste == False:
            raise IdNotExist
        
        return jsonify(data)
        
    except IdNotExist:
        return jsonify({'Error': 'O Id que você está procurando não existe'})

# ---- Rota Put Professores ---- #
@app.route("/professores/<id>", methods = ['PUT'])
def attProfessor(id):
    data = request.json
    idExiste = False
    try:
        for professor in professores:
            if professor['id'] == int(id):
                idExiste = True
                break
        
        if idExiste == False:
            raise IdNotExist
        
        if 'name' and 'age' and 'subject' and 'info' not in data:
            raise KeyError
        
        if data['name'] == "" or data['age'] == "" or data['subject'] == "" or data['info'] == "":
            raise EmptyStringError

        for professor in professores:
            if professor['id'] == int(id):
                professor['name'] = data['name']
                professor['age'] = data['age']
                professor['subject'] = data['subject']
                professor['info'] = data['info']
        
        return jsonify({'success': True})
    
    except IdNotExist:
        return jsonify({'Error': 'O Id que você quer atualizar não existe'})
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'})
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'})

# ---- Rota Delete Professores ---- #
@app.route("/professores/<id>", methods = ['DELETE'])
def deleteProfessor(id):
    idExiste = False
    try:
        for professor in professores:
            if professor['id'] == int(id):
                idExiste = True
                break
        
        if idExiste == False:
            raise IdNotExist

        for professor in professores:
            if professor['id'] == int(id):
                professores.remove(professor)
                professores_deletados.append(professor)
        
        return jsonify({'success': True})
    except IdNotExist:
        return jsonify({'Error': 'o Id que você quer deletar não existe'})

# ---- Rota Post Alunos ---- #
@app.route('/alunos', methods = ['POST'])
def addStudent():
    data = request.json
    try:
        if 'name' and 'age' and 'class' and 'bornDate' and 'firstGrade' and 'secondGrade' and 'finalAverage' not in data:
            raise KeyError
        
        if data['name'] == "" or data['age'] == "" or data['class'] == "" or data['bornDate'] == "" or data['firstGrade'] == "" or data['secondGrade'] == "" or data['finalAverage'] == "":
            raise EmptyStringError
                
        alunos.append({
            "name": data['name'], 
            "id": len(alunos) + len(alunos_deletados) + 1, 
            "age": data['age'], 
            "class": data['class'], 
            "bornDate": data['bornDate'], 
            "firstGrade": data['firstGrade'], 
            "secondGrade": data['secondGrade'],
            "finalAverage": data['finalAverage'] 
            })
        
        return jsonify({'success': True})
    
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'})
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'})

# ---- Rota Get Alunos ---- #
@app.route("/alunos", methods = ['GET'])
def getStudents():
    data = alunos
    return jsonify(data)

# ---- Rota Get Aluno Por ID ---- #
@app.route("/alunos/<id>", methods = ['GET'])
def getStudentById(id):
    data = {}
    idExiste = False
    try:
        for aluno in alunos:
            if aluno['id'] == int(id):
                data = aluno
                idExiste = True
                break
        
        if idExiste == False:
            raise IdNotExist
        
        return jsonify(data)
        
    except IdNotExist:
        return jsonify({'Error': 'O Id que você está procurando não existe'})

# ---- Rota Put Alunos ---- #
@app.route("/alunos/<id>", methods = ['PUT'])
def attStudent(id):
    data = request.json
    idExiste = False
    try:
        for aluno in alunos:
            if aluno['id'] == int(id):
                idExiste = True
                break
        
        if idExiste == False:
            raise Exception
        
        if 'name' and 'age' and 'class' and 'bornDate' and 'firstGrade' and 'secondGrade' and 'finalAverage' not in data:
            raise KeyError
        
        if data['name'] == "" or data['age'] == "" or data['class'] == "" or data['bornDate'] == "" or data['firstGrade'] == "" or data['secondGrade'] == "" or data['finalAverage'] == "":
            raise EmptyStringError

        for aluno in alunos:
            if aluno['id'] == int(id):
                aluno['name'] = data['name']
                aluno['age'] = data['age']
                aluno['class'] = data['class']
                aluno['bornDate'] = data['bornDate']
                aluno['firstGrade'] = data['firstGrade']
                aluno['secondGrade'] = data['secondGrade']
                aluno['finalAverage'] = data['finalAverage']
        
        return jsonify({'success': True})
    
    except Exception: 
        return jsonify({'Error': 'O Id que você quer atualizar não existe'})
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'})
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'})

# ---- Rota Delete Alunos ---- #
@app.route("/alunos/<id>", methods = ['DELETE'])
def deleteStudent(id):
    idExiste = False
    try:
        for aluno in alunos:
            if aluno['id'] == int(id):
                idExiste = True
                break

        if not idExiste:
            raise IdNotExist

        for aluno in alunos:
            if aluno['id'] == int(id):
                alunos.remove(aluno)
                alunos_deletados.append(aluno)

        return jsonify({'success': True})
    except IdNotExist:
        return jsonify({'Error': 'O Id que você quer deletar não existe'})

# ---- Rota Post Turmas ---- #
@app.route("/turmas", methods = ['POST'])
def addTurmas():
    data = request.json
    try:
        if 'name' and 'professor' and 'status' not in data:
            raise KeyError
        
        if data['name'] == "" or data['professor'] == "" or data['status'] == "":
            raise EmptyStringError

        turmas.append({
            "id": len(turmas) + len(turmas_deletadas) + 1, 
            "name": data['name'], 
            "professor": data['professor'], 
            "status": data['status']
            })
        
        return jsonify({'success': True})
    
    except EmptyStringError:
        return jsonify({'Error': 'As chaves não podem estar vazias'})
    except KeyError:
        return jsonify({'Error': 'Você não passou alguma chave'})

# ---- Rota Get Turmas ---- #
@app.route("/turmas", methods = ["GET"])
def getClasses():
    data = turmas
    return jsonify(data)

# ---- Rota Get Turmas Por ID ---- #
@app.route("/turmas/<id>", methods = ['GET'])
def getClassById(id):
    data = {}
    idExiste = False
    try:
        for turma in turmas:
            if turma['id'] == int(id):
                data = turma
                idExiste = True
                break
        
        if idExiste == False:
            raise IdNotExist
        
        return jsonify(data)
        
    except IdNotExist:
        return jsonify({'Error': 'O Id que você está procurando não existe'})

# ---- Rota Get Turmas Por ID ---- #
@app.route("/turmas/<id>", methods = ['GET'])
def getClassById(id):
    data = {}
    for turma in turmas:
        if turma['id'] == int(id):
            data = turma
            break
    
    return jsonify(data)

# ---- Rota Delete Turmas ---- #
@app.route("/turmas/<id>", methods = ["DELETE"])
def deleteClass(id):
    for turma in turmas:
        if turma['id'] == int(id):
            turmas.remove(turma)
    
    return jsonify({'success': True})

# ---- Rota Para Resetar As Listas ---- #
@app.route("/reseta", methods = ["POST"])
def resetArrays():
    alunos.clear()
    professores.clear()
    turmas.clear()

    return jsonify({'success': True})
    
if __name__ == '__main__':
    app.run(debug=True)