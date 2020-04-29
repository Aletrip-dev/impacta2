# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
#
# e-mail: nome.sobrenome@aluno.faculdadeimpacta.com.br

from typing import Dict, List


class Pessoa:
    '''
    Classe Abstrata Pessoa - não deve ser alterada
    '''
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    Métodos que tenham exatamente a mesma implementação em todas as classes filhas
    podem ser editados nesta classe, por exemplo consulta_carga_horaria, que sempre retorna
    o valor de carga horária salvo no objeto. No entanto, todos os métodos que tenham uma
    implementação específica para dada classe, devem ser sobrescrito em tais classes.
    '''
    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        '''
        Construtor da classe Funcionário - lembre-se de usar o super para acessar o construtor da classe mãe
        e criar atributos que já estão definidos lá.
        '''
        super().__init__(nome,idade)
        self.emal = email
        self.carga_horaria_semanal = carga_horaria_semanal
        self.sal_base = 0
        self.semanas = 4.5
        self.carga_h = 0

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        self.salario =  self.sal_base * self.semanas * self.carga_h
        raise NotImplementedError

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        self.carga_horaria_semanal = nova_carga_horaria
        raise NotImplementedError

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.consulta_carga_horaria
        raise NotImplementedError

    def aumenta_salario(self) -> None:
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        aumento =  (self.sal_base * self.carga_horaria_semanal * self.semanas)*1.05
        return aumento
        raise NotImplementedError


'''
DICAS:

Se uma classe não possui um método definido, mas este método é definido em
alguma classe mãe acima, a classe irá herdar e usar tal método exatamente como
ele está definido na classe acima.

Isto também se aplica ao construtor, se Programador não define um __init__, então
esta classe está automaticamente usando o __init__ da classe Funcionário (se
funcionário tampouco definisse um __init__, então seria usado o de Pessoa, e se
pessoa tampouco o fizesse, seria usado o de Object, que é a classe base do Python
usada automaticamente para todos as classes que criamos).

Caso você queira ou precise adicionar atributos extras na classe Programador
(ou qualquer outra classe filha de Funcionário), defina o método construtor,
faça a utilização do super e adicione os atributos extra que serão específicos
daquela classe, sejam eles recebidos por parâmetros ou não.

Lembrando sempre que o enunciado define quais são os parâmetros obrigatórios
de uma classe, então se forem criados parâmetros obrigatórios extras, isso
irá gerar erros nos testes de correção.
'''


class Programador(Funcionario):
    '''
    Funcionário do tipo programador:
    - salario base por hora 35.00;
    - regime de trabalho entre 20h e 40h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal e considere que o mês
      possui sempre 4.5 semanas.
    '''
    # Define a carga horária

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):

        self.semanas = 4.5
        self.sal_base = 35.00
        self.carga_h = 0
        self.carga_horaria_semanal = carga_horaria_semanal
        if self.carga_horaria_semanal < 20 or self.carga_horaria_semanal > 40:
            raise ValueError('Carga Horária Semanal Inválida')
        pass
    
    #salário

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        salario =  self.sal_base * self.carga_horaria_semanal * self.semanas
        return salario

    #carga horária

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.carga_horaria_semanal


    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''

        if nova_carga_horaria < 20 or nova_carga_horaria > 40:
            raise ValueError('Carga Horária Semalan Inválida')
        self.carga_horaria_semanal = nova_carga_horaria

    def aumenta_salario(self) -> None:
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        reajuste = self.sal_base * 0.05
        self.sal_base = self.sal_base + reajuste
        

class Estagiario(Funcionario):
    '''
    Funcionário do tipo estagiário:
    - salario base por hora 15.50;
    - auxilio alimentação fixo de 250 reais por mês;
    - regime de trabalho deve estar entre 16h e 30h semanais, caso contrário levanta um ValueError;
    - cálculo do sálario mensal: calcule o pagamento semanal, considere que o mês
      possui sempre 4.5 semanas, e por fim adicione o auxílio alimentação.
    '''
    # Define a carga horária

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        self.semanas = 4.5
        self.sal_base = 15.50
        self.aux_alim = 250
        self.carga_horaria_semanal = carga_horaria_semanal
        if self.carga_horaria_semanal < 16 or self.carga_horaria_semanal > 30:
            raise ValueError('Carga Horária Semalan Inválida')
        pass

   #salário
    
    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        salario =  self.sal_base * self.carga_horaria_semanal * self.semanas + self.aux_alim
        return salario

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.carga_horaria_semanal


    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        self.carga_horaria_semanal = nova_carga_horaria

    def aumenta_salario(self) -> None:
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        reajuste = self.sal_base * 0.05
        self.sal_base = self.sal_base + reajuste
        
    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''

        if nova_carga_horaria < 16 or nova_carga_horaria > 30:
            raise ValueError('Carga Horária Semalan Inválida')
        self.carga_horaria_semanal = nova_carga_horaria

class Vendedor(Funcionario):
    '''
    Funcionário do tipo vendedor:
    - salario base por hora 30.00;
    - auxilio alimentação fixo de 350 reais por mês;
    - auxilio transporte fixo de 30 reais por visita realizada ao cliente;
    - regime de trabalho deve estar entre 15h e 45h semanais, caso contrário
      levanta um ValueError;
    - possui um atributo privado que guarda o número de visitas realizadas no mês,
      começando sempre em zero;
    - cálculo do sálario mensal: calcule o pagamento semanal, considere que o mês
      possui sempre 4.5 semanas, e por fim calcule e adicione os auxílios;
    - além dos métodos de Funcionário, deve implementar os métodos:
      * realizar_visita; e
      * zerar_visitas.
    '''
    # Define a carga horária

    def __init__(self, nome: str, idade: int, email: str, carga_horaria_semanal: int):
        self.__s_visitas = 0
        self.semanas = 4.5
        self.sal_base = 30.00
        self.aux_alim = 350
        self.aux_trans = 0
        self.carga_horaria_semanal = carga_horaria_semanal
        if self.carga_horaria_semanal < 15 or self.carga_horaria_semanal > 45:
            raise ValueError('Carga Horária Semalan Inválida')
        pass

   #salário
    
    def calcula_salario(self) -> float:
        '''
        Calcula o salário do mês para o funcionário
        '''
        salario =  self.sal_base * self.carga_horaria_semanal * self.semanas + self.aux_alim + self.aux_trans
        return salario

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.carga_horaria_semanal

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''
        self.carga_horaria_semanal = nova_carga_horaria

    def aumenta_salario(self) -> None:
        '''
        Aplica um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        reajuste = self.sal_base * 0.05
        self.sal_base = self.sal_base + reajuste
        
    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite de horas por categoria.
        Caso o numero informado seja inválido, levanta um ValueError
        '''

        if nova_carga_horaria < 15 or nova_carga_horaria > 45:
            raise ValueError('Carga Horária Semalan Inválida')
        self.carga_horaria_semanal = nova_carga_horaria      

    def consulta_visitas(self) -> int:
        """
        Retorna o número de visitas realizadas pelo vendedor até o momento
        """
        return self.__s_visitas

    def realizar_visita(self, n_visitas: int) -> None:
        '''
        Recebe um número inteiro e incrementa o número de visitas realizadas no mês
        com o valor recebido. Antes de fazer a alteração, verifique se n_visitas é
        um número inteiro e levante um TypeError caso contrário; Em seguida verifique
        se n_visitas é positivo e maior que zero, levantando um ValueError caso contrário.
        '''

        if type(n_visitas) != int:
            raise TypeError
        elif n_visitas <= 0:
            raise ValueError
        else:
            self.__s_visitas += n_visitas
            self.aux_trans += n_visitas * 30




    def zerar_visitas(self) -> None:
        '''
        Quando chamado deve redefinir o número de visitas realizadas pelo vendedor para zero,
        de modo a começar a contagem para o mês seguinte.
        '''
        self.__s_visitas = 0


class Empresa:
    '''
    Classe empresa, gerencia diversos funcionários
    '''
    def __init__(self, nome: str, cnpj: int, area_atuacao: str,
                 equipe: List[Funcionario] = []):
        '''
        Construtor da classe empresa
        '''
        self.empresa_nome = nome
        self.empresa_cnpj = cnpj
        self.empresa_rea_atuacao = area_atuacao
        self.funcionarios = equipe




    def contrata(self, novo_funcionario: Funcionario) -> None:
        '''
        Contrata um novo funcionário para a empresa (adicionando ele à lista de funcionários)
        '''
        novo_funcionario = ['Alex', 38, 'alex@alex.com.br',40]
        self.lista_fucionarios.append(novo_funcionario)

    def lista_fucionarios(self) -> List[Funcionario]:
        '''
        Devolve um lista com todos os funcionarios
        '''
        return self.funcionarios

    def folha_pagamento(self) -> float:
        '''
        Devolve o valor total gasto com o pagamento de todos os funcionários
        DICA: Itere sobre a lista de funcionários, fazendo cada objeto do tipo Funcionário
        calcular o próprio salário e acumule isso numa variável auxiliar.
        '''
        pass

    def dissidio_anual(self) -> None:
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários
        DICA: idem ao método de folha de pagamento, percorra a lista de funcionários faça
        cada objeto funcionário aumentar o próprio salário base por hora.
        '''
        pass

    def listar_visitas(self) -> Dict[str, int]:
        '''
        Retorna um dicionário com as visitas realizadas por cada vendedor;
        Como a chave do dicionário precisa ser única, deve ser usado o email do vendedor
        e o valor deve ser o número de visitas realizadas por aquele funcionário.
        DICA: percorra a lista de funcionários e use o operador 'is' para verificar se
        o funcionário é um vendedor, em caso positivo, adicione as informações pedidas
        ao dicionário, e por fim retorne esse dicionário (não precisa guardar em um atributo).
        '''
        pass

    def zerar_visitas_vendedores(self) -> None:
        '''
        Zera as visitas de todos os funcionário, use a dica do método listar_visitas e
        para cada vendedor, chame o método de zerar visitas do vendedor.
        '''
        pass
