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
        
    # ---- Testa se o DELETE da rota /alunos deleta o aluno do id selecionado ---- #
    def test_004_deleta_alunos(self):
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
        requests.post('http://localhost:5000/alunos',json={
            "name": "Kaio",
            "age": 18, 
            "class": 1, 
            "bornDate": "10/04/2006", 
            "firstGrade": 5, 
            "secondGrade": 9,
            "finalAverage": 7 
            })
        
        r_lista = requests.get('http://localhost:5000/alunos')
        lista_retornada = r_lista.json()
        
        self.assertEqual(len(lista_retornada),3)
        
        requests.delete('http://localhost:5000/alunos/2')
        
        r_lista2 = requests.get('http://localhost:5000/alunos')
        lista_retornada2 = r_lista2.json()
        
        self.assertEqual(len(lista_retornada2),2) 

        acheiFabio = False
        acheiKaio = False
        for aluno in lista_retornada:
            if aluno['name'] == 'Fábio':
                acheiFabio=True
            if aluno['name'] == 'Kaio':
                acheiKaio=True
        if not acheiFabio or not acheiKaio:
            self.fail("Você pode ter deletado o aluno errado!")

        requests.delete('http://localhost:5000/alunos/1')

        r_lista3 = requests.get('http://localhost:5000/alunos')
        lista_retornada3 = r_lista3.json()
        
        self.assertEqual(len(lista_retornada3),1) 

        if lista_retornada3[0]['name'] == 'Kaio':
            pass
        else:
            self.fail("Você pode ter deletado o aluno errado!")

    # ---- Testa se o PUT da rota /alunos atualiza o aluno do id selecionado ---- #
    def test_005_edita_alunos(self):
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
            "name": "Diego",
            "age": 22, 
            "class": 1, 
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        requests.post('http://localhost:5000/alunos',json={
            "name": "Bruna",
            "age": 19, 
            "class": 1, 
            "bornDate": "30/01/2006", 
            "firstGrade": 2,
            "secondGrade": 9,
            "finalAverage": 4.5 
            })
        
        r_antes = requests.get('http://localhost:5000/alunos/2')
        
        self.assertEqual(r_antes.json()['name'],'Bruna')

        requests.put('http://localhost:5000/alunos/2', json={
            "name": "Brunasser",
            "age": 19, 
            "class": 1, 
            "bornDate": "30/01/2006", 
            "firstGrade": 2,
            "secondGrade": 9,
            "finalAverage": 4.5 
            })
        
        r_depois = requests.get('http://localhost:5000/alunos/2')
        
        self.assertEqual(r_depois.json()['name'],'Brunasser')
        self.assertEqual(r_depois.json()['age'],19)
        
    # ---- Testa se o GET retorna todos os alunos ---- #
    def test_006_retorna_todos_alunos(self):
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
            "name": "Fábio",
            "age": 20, 
            "class": 1, 
            "bornDate": "18/09/2004", 
            "firstGrade": 2, 
            "secondGrade": 4,
            "finalAverage": 3 
            })
        requests.post('http://localhost:5000/alunos',json={
            "name": "Kaio",
            "age": 18, 
            "class": 1, 
            "bornDate": "10/04/2006", 
            "firstGrade": 5, 
            "secondGrade": 9,
            "finalAverage": 7 
            })
        
        acheiFabio = False
        acheiKaio = False

        r_lista = requests.get('http://localhost:5000/alunos')
        lista_retornada = r_lista.json()

        for aluno in lista_retornada:
            if aluno['name'] == 'Fábio':
                acheiFabio=True
            if aluno['name'] == 'Kaio':
                acheiKaio=True
        if not acheiFabio or not acheiKaio:
            self.fail("Não retornou todos os alunos")

        self.assertEqual(len(lista_retornada),2)

    # ---- Testa se as rotas em que precisa passar um id retorna o erro falando que não existe o id selecionado ---- #
    def test_007_id_inexistente_alunos(self):
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

        # ---- Adicionando aluno ---- #
        requests.post('http://localhost:5000/alunos',json={
            "name": "Fábio",
            "age": 22,
            "class": 1,
            "bornDate": "18/09/2004",
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })

        # ---- Rota PUT ---- #
        r = requests.put('http://localhost:5000/alunos/30',json={
            "name": "Fábio",
            "age": 20, 
            "class": 1, 
            "bornDate": "18/09/2004", 
            "firstGrade": 2, 
            "secondGrade": 4,
            "finalAverage": 3 
            })

        self.assertEqual(r.json()['Error'],'O Id que você quer atualizar não existe')

        # ---- Rota GET ---- #
        r = requests.get('http://localhost:5000/alunos/50')
        
        self.assertEqual(r.json()['Error'],'O Id que você está procurando não existe')

        # ---- Rota DELETE ---- #
        r = requests.delete('http://localhost:5000/alunos/50')
        
        self.assertEqual(r.json()['Error'],'O Id que você quer deletar não existe')

    # ---- Testa se o PUT e o POST retornam o erro que as chaves não podem tem valores vazios ---- #
    def test_008_atualiza_ou_adiciona_aluno_com_valores_vazios(self):
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

        # ---- Adicionando aluno ---- #
        requests.post('http://localhost:5000/alunos',json={
            "name": "Diego",
            "age": 22, 
            "class": 1, 
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })

        # ---- Chave name com valor vazio ---- #
        r = requests.put('http://localhost:5000/alunos/1',json={
            "name": "",
            "age": 22, 
            "class": 1, 
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        
        self.assertEqual(r.json()['Error'],'As chaves não podem estar vazias')

        # ---- Chave bornDate com valor vazio ---- #
        r = requests.post('http://localhost:5000/alunos',json={
            "name": "Fábio",
            "age": 22, 
            "class": 1, 
            "bornDate": "", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        
        self.assertEqual(r.json()['Error'],'As chaves não podem estar vazias')

    # ---- Testa se o PUT e o POST retornam o erro que está faltando alguma chave no request ---- #
    def test_009_atualiza_ou_adiciona_aluno_sem_alguma_chave(self):
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

        # ---- Adicionando aluno ---- #
        requests.post('http://localhost:5000/alunos',json={
            "name": "Diego",
            "age": 22,
            "class": 1, 
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        
        # ---- PUT sem a chave class ---- #
        r = requests.put('http://localhost:5000/alunos/1',json={
            "name": "Fábio",
            "age": 22,
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        
        self.assertEqual(r.json()['Error'],'Você não passou alguma chave')
        
        # ---- POST sem a chave firstGrade ---- #
        r = requests.post('http://localhost:5000/alunos',json={
            "name": "Luiz",
            "age": 18, 
            "class": 1, 
            "bornDate": "25/06/2006", 
            "secondGrade": 7,
            "finalAverage": 6 
            })
        
        self.assertEqual(r.json()['Error'],'Você não passou alguma chave')

    # ---- Teste para ver se retorna o erro que o id da classe passada não existe ---- #
    def test_010_atualiza_ou_adiciona_aluno_com_classe_inexistente(self):
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

        # ---- Adicionando aluno ---- #
        requests.post('http://localhost:5000/alunos',json={
            "name": "Fábio",
            "age": 20, 
            "class": 1, 
            "bornDate": "18/09/2004",
            "firstGrade": 2, 
            "secondGrade": 4,
            "finalAverage": 3 
            })
        
        r = requests.put('http://localhost:5000/alunos/1',json={
            "name": "Fábio",
            "age": 22,
            "class": 60,
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        
        self.assertEqual(r.json()['Error'],'O Id de classe não existe')

        r = requests.post('http://localhost:5000/alunos',json={
            "name": "Diego",
            "age": 22,
            "class": 50, 
            "bornDate": "28/06/2002", 
            "firstGrade": 10, 
            "secondGrade": 9,
            "finalAverage": 9.5 
            })
        
        self.assertEqual(r.json()['Error'],'O Id de classe não existe')

    # ---- Testa se o POST da rota /professores está adicionando os professores ---- #
    def test_011_adiciona_professores(self):
        requests.post('http://localhost:5000/professores',json={
            "name": "Caio",
            "age": 26,
            "subject": "API e Microserviços",
            "info": "Tem tatuagem"
            })
        requests.post('http://localhost:5000/professores',json={
            "name": "Odair",
            "age": 26,
            "subject": "DevOps",
            "info": "Usa óculos"
            })
        
        r_lista = requests.get('http://localhost:5000/professores')
        lista_retornada = r_lista.json()

        achei_caio = False
        achei_odair = False
        for professor in lista_retornada:
            if professor['name'] == 'Caio':
                achei_caio = True
            if professor['name'] == 'Odair':
                achei_odair = True
        
        if not achei_caio:
            self.fail('Professor Caio não apareceu na lista de professores')
        if not achei_odair:
            self.fail('Professor Odair não apareceu na lista de professores')

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()