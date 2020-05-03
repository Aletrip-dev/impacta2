# e1 = ['Rio de Janeiro', 'RJ']
# e2 = ['São Paulo','SP']
# m1 = ['Taboão', 'SP']
# m2 = ['Pitiruta', 'SP']
class Pais:
    def __init__(self, nome: str):
        self.nome = nome

    def estado(self, nome:str, uf:str):
        self.nome = nome
        self.uf = uf

    def municipio(self, nome:str, uf:str):
        self.nome = nome
        self.uf = uf

def cadastra_estado(self, est:str):
    est = []
    for c in est:
        e1= str(input('Informe um estado: '))
