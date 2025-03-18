from flask import Flask, jsonify, request

app = Flask(__name__)
professores = []
alunos = []
turmas = []

# ---- Rota Post Professores ---- #
@app.route('/professores', methods = ['POST'])
def addProfessor():
    data = request.json

    professores.append({
        "name": data['name'], 
        "id": len(professores) + 1, 
        "age": data['age'], 
        "subject": data['subject'], 
        "info": data['info']
        })
    
    return jsonify({'success': True})

# ---- Rota Get Professores ---- #
@app.route("/professores", methods = ['GET'])
def getProfessors():
    data = professores
    return jsonify(data)

# ---- Rota Put Professores ---- #
@app.route("/professores/<id>", methods = ['PUT'])
def attProfessor(id):
    data = request.json
    
    for professor in professores:
        if professor['id'] == int(id):
            professor['name'] = data['name']
            professor['age'] = data['age']
            professor['subject'] = data['subject']
            professor['info'] = data['info']

    return jsonify({'success': True})

# ---- Rota Get Professor Por ID ---- #
@app.route("/professores/<id>", methods = ['GET'])
def getProfessorById(id):
    data = {}
    for professor in professores:
        if professor['id'] == int(id):
            data = professor
            break
        
    return jsonify(data)

# ---- Rota Delete Professores ---- #
@app.route("/professores/<id>", methods = ['DELETE'])
def deleteProfessor(id):
    for professor in professores:
        if professor['id'] == int(id):
            professores.remove(professor)
        
    return jsonify({'success': True})

# ---- Rota Post Alunos ---- #
@app.route('/alunos', methods = ['POST'])
def addStudent():
    data = request.json
    
    alunos.append({
        "name": data['name'], 
        "id": len(alunos) + 1, 
        "age": data['age'], 
        "class": data['class'], 
        "bornDate": data['bornDate'], 
        "firstGrade": data['firstGrade'], 
        "secondGrade": data['secondGrade'],
        "finalAverage": data['finalAverage'] 
        })
    
    return jsonify({'success': True})

# ---- Rota Get Alunos ---- #
@app.route("/alunos", methods = ['GET'])
def getStudents():
    data = alunos
    return jsonify(data)

# ---- Rota Put Alunos ---- #
@app.route("/alunos/<id>", methods = ['PUT'])
def attStudent(id):
    data = request.json
           
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

# ---- Rota Get Aluno Por ID ---- #
@app.route("/alunos/<id>", methods = ['GET'])
def getStudentById(id):
    data = {}
    
    for aluno in alunos:
        if aluno['id'] == int(id):
            data = aluno
            break
        
    return jsonify(data)

# ---- Rota Delete Alunos ---- #
@app.route("/alunos/<id>", methods = ['DELETE'])
def deleteStudent(id):
    for aluno in alunos:
        if aluno['id'] == int(id):
            alunos.remove(aluno)

    return jsonify({'success': True})

# ---- Rota Post Turmas ---- #
@app.route("/turmas", methods = ['POST'])
def addTurmas():
    data = request.json
    
    turmas.append({
        "id": len(turmas) + 1, 
        "name": data['name'], 
        "professor": data['professor'], 
        "status": data['status']
        })
    
    return jsonify({'success': True})
    
if __name__ == '__main__':
    app.run(debug=True)