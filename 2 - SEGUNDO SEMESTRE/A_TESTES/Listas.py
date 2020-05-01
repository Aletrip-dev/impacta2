from typing import Dict, List


class Funcionario:
    def __init__(self, nome: str, email: str, idade: int):
        self.nome = nome
        self.email = email
        self.idade = idade

class Analista(Funcionario):
    def __init__(self, nome: str, email: str, idade: int): #Deve conter os mesmos atributos da classe mãe (fucnionários)
        super().__init__(nome, email, idade) #Herda os atributos da classe funcionário - não sendo necessário informar novamente

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, idade: int, atuacao: str): #Deve conter os mesmos atributos da classe mãe (fucnionários)
        super().__init__(nome, email, idade) #Herda os atributos da classe funcionário - não sendo necessário informar novamente
        self.atuacao = atuacao

class Empresa:
    def __init__(self, nome: str, relacao: List[Funcionario] = []):
        self.nome = nome
        self.relacao = relacao #recebe a lista da classe mãe (FUNCIONÁRIOS)

    def adiciona(self, func: Funcionario):
        self.relacao.append(func) #Adiciona o funcionário à empresa

    def lista_func(self):
        return self.relacao#retorna a lista


#INSTANCIANDO

emp = Empresa('EcoUrbis',[])
f1 = Analista('Alex','email@email.com',38)
f2 = Analista('João','email@email.com',55)
f3 = Gerente('Olsen','email@email.com',38,'Gerencia Operacional')

emp.adiciona(f1)
emp.adiciona(f2)
emp.adiciona(f3)

lista = emp.lista_func()

indice = 0
for v in lista:
    indice += 1
    if isinstance(v, Gerente):
        print(f'{indice} --> {emp.nome} --> {v.nome},{v.email},{v.idade},{v.atuacao}')
    else:
        print(f'{indice} --> {emp.nome} --> {v.nome},{v.email},{v.idade}')