from errors import EmptyStringError, IdNotExist
from professor.professor_model import professores

turmas = []
turmas_deletadas = []

def addClass(data):
    professorExiste = False

    if 'name' and 'professor' and 'active' not in data:
        raise KeyError
    
    if data['name'] == "" or data['professor'] == "" or data['active'] == "":
        raise EmptyStringError
    
    for professor in professores:
        if professor['id'] == data['professor']:
            professorExiste = True
            break

    if not professorExiste:
        raise IdNotExist('O Id de professor não existe')

    turmas.append({
        "id": len(turmas) + len(turmas_deletadas) + 1, 
        "name": data['name'], 
        "professor": data['professor'], 
        "active": data['active']
        })
    
def getClasses():
    return turmas

def getClassById(id):
    data = {}
    idExiste = False

    for turma in turmas:
        if turma['id'] == int(id):
            data = turma
            idExiste = True
            break
    
    if not idExiste:
        raise IdNotExist('O Id que você está procurando não existe')
    
    return data

def attClass(id, data):
    idExiste = False
    professorExiste = False

    for turma in turmas:
        if turma['id'] == int(id):
            idExiste = True
            break

    if not idExiste:
        raise IdNotExist('O Id que você quer atualizar não existe')
    
    if 'name' and 'professor' and 'active' not in data:
        raise KeyError
    
    if data['name'] == "" or data['professor'] == "" or data['active'] == "":
        raise EmptyStringError
    
    for professor in professores:
        if professor['id'] == data['professor']:
            professorExiste = True
            break

    if not professorExiste:
        raise IdNotExist('O Id de professor não existe')

    for turma in turmas:
            if turma['id'] == int(id):
                turma['name'] = data['name']
                turma['professor'] = data['professor']
                turma['active'] = data['active']

def deleteClass(id):
    idExiste = False

    for turma in turmas:
        if turma['id'] == int(id):
            idExiste = True
            break

    if not idExiste:
        raise IdNotExist('O Id que você quer deletar não existe')

    for turma in turmas:
        if turma['id'] == int(id):
            turmas.remove(turma)
            turmas_deletadas.append(turma)
