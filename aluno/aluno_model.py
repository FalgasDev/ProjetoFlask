from errors import EmptyStringError, IdNotExist
from turma.turma_model import turmas

alunos = []
alunos_deletados = []

def addStudent(data):
    classeExiste = False

    if 'name' and 'age' and 'class' and 'bornDate' and 'firstGrade' and 'secondGrade' and 'finalAverage' not in data:
        raise KeyError
        
    if data['name'] == "" or data['age'] == "" or data['class'] == "" or data['bornDate'] == "" or data['firstGrade'] == "" or data['secondGrade'] == "" or data['finalAverage'] == "":
        raise EmptyStringError
    
    for turma in turmas:
        if turma['id'] == data['class']:
            classeExiste = True
            break

    if not classeExiste:
        raise IdNotExist('O Id de classe não existe')
            
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
    
def getStudents():
    return alunos

def getStudentById(id):
    data = {}
    idExiste = False

    for aluno in alunos:
        if aluno['id'] == int(id):
            data = aluno
            idExiste = True
            break
    
    if not idExiste:
        raise IdNotExist('O Id que você está procurando não existe')
    
    return data

def attStudent(id, data):
    idExiste = False
    classeExiste = False

    for aluno in alunos:
        if aluno['id'] == int(id):
            idExiste = True
            break
    
    if not idExiste:
        raise IdNotExist('O Id que você quer atualizar não existe')
    
    if 'name' and 'age' and 'class' and 'bornDate' and 'firstGrade' and 'secondGrade' and 'finalAverage' not in data:
        raise KeyError
    
    if data['name'] == "" or data['age'] == "" or data['class'] == "" or data['bornDate'] == "" or data['firstGrade'] == "" or data['secondGrade'] == "" or data['finalAverage'] == "":
        raise EmptyStringError
    
    for turma in turmas:
        if turma['id'] == data['class']:
            classeExiste = True
            break

    if not classeExiste:
        raise IdNotExist('O Id de classe não existe')

    for aluno in alunos:
        if aluno['id'] == int(id):
            aluno['name'] = data['name']
            aluno['age'] = data['age']
            aluno['class'] = data['class']
            aluno['bornDate'] = data['bornDate']
            aluno['firstGrade'] = data['firstGrade']
            aluno['secondGrade'] = data['secondGrade']
            aluno['finalAverage'] = data['finalAverage']

def deleteStudent(id):
    idExiste = False

    for aluno in alunos:
        if aluno['id'] == int(id):
            idExiste = True
            break

    if not idExiste:
        raise IdNotExist('O Id que você quer deletar não existe')

    for aluno in alunos:
        if aluno['id'] == int(id):
            alunos.remove(aluno)
            alunos_deletados.append(aluno)