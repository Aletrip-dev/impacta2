from Listas import Empresa, Analista

def test_Verifica_Lista():
    emp = Empresa('EcoUrbis',[])
    f1 = Analista('Alex','email@email.com',38)
    f2 = Analista('João','email@email.com',55)
    emp.adiciona(f1)
    emp.adiciona(f2)
    lista = emp.lista_func()
    assert len(lista) == 2, 'Lista de funcionários não contém o número correto de funcionários contratados'
