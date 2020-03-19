class veiculo():

    @motorizacao # indica que é uma propriedade do veículo
    def motorizacao(self): #métdodo para leitura da propriedade
        return self.motorizacao

    @motorizacao.setter #seta para que receba um valor
    def motorizacaoI(self, value):
        self.__motorizacao  = value

    def ligar(self):
        return True
    
    def brecar(self):
        return True


Fusca = veiculo()
Fusca.ligar()
Fusca.brecar()
Fusca.motorizacao = 2000
print(Fusca.motorizacao)