from flask import Flask, jsonify, request

app = Flask(__name__)
professores = []

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

if __name__ == '__main__':
    app.run(debug=True)