import requests
import unittest

class TestStringMethods(unittest.TestCase):
    # ---- Testa se o GET da rota /alunos devolve uma lista ---- #
    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5000/alunos')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /alunos no seu server")

        try:
            obj_retornado = r.json()

        except:
            self.fail("queria um json mas voce retornou outra coisa")

        self.assertEqual(type(obj_retornado),type([]))

    # ---- Testa se o POST da rota /alunos está adicionando os alunos ---- #
    def test_001_adiciona_alunos(self):
        # ---- Adicionando professor ---- #
        requests.post('http://localhost:5000/professores',json={
            "name": "Caio",
            "age": 26,
            "subject": "API e Microserviços",
            "info": "Tem tatuagem"
            })
        
        # ---- Adicionando turma ---- #
        requests.post('http://localhost:5000/turmas',json={
            "name": "Desenvolvimento de API e Microserviços",
            "professor": 1,
            "active": True
            })

        # ---- Adicionando alunos ---- #
        requests.post('http://localhost:5000/alunos',json={
            "name": "Fábio",
            "age": 20, 
            "class": 1, 
            "bornDate": "18/09/2004", 
            "firstGrade": 2, 
            "secondGrade": 4,
            "finalAverage": 3 
            })
        requests.post('http://localhost:5000/alunos',json={
            "name": "Luiz",
            "age": 18, 
            "class": 1, 
            "bornDate": "25/06/2006", 
            "firstGrade": 5, 
            "secondGrade": 7,
            "finalAverage": 6 
            })
        
        r_lista = requests.get('http://localhost:5000/alunos')
        lista_retornada = r_lista.json()

        achei_fabio = False
        achei_luiz = False
        for aluno in lista_retornada:
            if aluno['name'] == 'Fábio':
                achei_fabio = True
            if aluno['name'] == 'Luiz':
                achei_luiz = True
        
        if not achei_fabio:
            self.fail('aluno fernando nao apareceu na lista de alunos')
        if not achei_luiz:
            self.fail('aluno roberto nao apareceu na lista de alunos')
            
    # ---- Testa se o GET da rota /alunos devolve o aluno do id selecionado ---- #
    def test_002_aluno_por_id(self):
        r_reset = requests.post('http://localhost:5000/reseta')
        self.assertEqual(r_reset.status_code,200)

        # ---- Adicionando professor ---- #
        requests.post('http://localhost:5000/professores',json={
            "name": "Caio",
            "age": 26,
            "subject": "API e Microserviços",
            "info": "Tem tatuagem"
            })
        
        # ---- Adicionando turma ---- #
        requests.post('http://localhost:5000/turmas',json={
            "name": "Desenvolvimento de API e Microserviços",
            "professor": 1,
            "active": True
            })

        # ---- Adicionando alunos ---- #
        requests.post('http://localhost:5000/alunos',json={
            "name": "Kaio",
            "age": 18, 
            "class": 1, 
            "bornDate": "10/04/2006", 
            "firstGrade": 5, 
            "secondGrade": 9,
            "finalAverage": 7 
            })
        requests.post('http://localhost:5000/alunos',json={
            "name": "Diego",
            "age": 22, 
            "class": 1, 
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })

        resposta = requests.get('http://localhost:5000/alunos/2')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado),dict)
        self.assertIn('name',dict_retornado)
        
        self.assertEqual(dict_retornado['name'],'Diego')
        
    # ---- Testa se a rota /reseta apaga todos os dados da lista professores ---- #
    def test_003_reseta(self):
        requests.post('http://localhost:5000/professores',json={
            "name": "Caio",
            "age": 26,
            "subject": "API e Microserviços",
            "info": "Tem tatuagem"
            })
        
        r_lista = requests.get('http://localhost:5000/professores')

        self.assertTrue(len(r_lista.json()) > 0)

        r_reset = requests.post('http://localhost:5000/reseta')

        self.assertEqual(r_reset.status_code,200)

        r_lista_depois = requests.get('http://localhost:5000/professores')
        
        self.assertEqual(len(r_lista_depois.json()),0)

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()