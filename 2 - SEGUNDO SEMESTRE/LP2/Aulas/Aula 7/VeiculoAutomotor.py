from Frenagem import Frenagem
from Ignicao import Ignicao

class VeiculoAutomotor(Frenagem, Ignicao):

    def Buzinar(self, vezes):
        return vezes

    def Brecar(self):
        return super().Brecar()

