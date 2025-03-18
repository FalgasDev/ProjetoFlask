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

if __name__ == '__main__':
    app.run(debug=True)