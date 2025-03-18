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

if __name__ == '__main__':
    app.run(debug=True)