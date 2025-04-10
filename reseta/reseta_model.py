from aluno.aluno_model import alunos, alunos_deletados
from professor.professor_model import professores, professores_deletados
from turma.turma_model import turmas, turmas_deletadas

def resetArrays():
    alunos.clear()
    professores.clear()
    turmas.clear()
    professores_deletados.clear()
    alunos_deletados.clear()
    turmas_deletadas.clear()