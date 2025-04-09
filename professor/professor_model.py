from errors import EmptyStringError, IdNotExist

professores = []
professores_deletados = []

def addProfessor(data):
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
    
def getProfessors():
    return professores

def getProfessorById(id):
    data = {}
    idExiste = False

    for professor in professores:
        if professor['id'] == int(id):
            data = professor
            idExiste = True
            break
        
    if not idExiste:
        raise IdNotExist('O Id que você está procurando não existe')
    
    return data

def attProfessor(id, data):
    idExiste = False

    for professor in professores:
        if professor['id'] == int(id):
            idExiste = True
            break
        
    if not idExiste:
        raise IdNotExist('O Id que você quer atualizar não existe')
    
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

def deleteProfessor(id):
    idExiste = False

    for professor in professores:
        if professor['id'] == int(id):
            idExiste = True
            break
    
    if not idExiste:
        raise IdNotExist('O Id que você quer deletar não existe')

    for professor in professores:
        if professor['id'] == int(id):
            professores.remove(professor)
            professores_deletados.append(professor)