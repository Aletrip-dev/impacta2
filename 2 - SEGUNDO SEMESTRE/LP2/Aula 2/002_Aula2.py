def credito(valor):
    valor = valor * 2
    return valor

def debito(valor):
    valor = valor / 10
    return valor

custo = 150

print(debito(custo))
print(credito(custo))