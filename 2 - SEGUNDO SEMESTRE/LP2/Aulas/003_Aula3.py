#listas
'''dados = [1,2,3]
mult = dados[1] * dados[2]
print (mult)'''

#dicionários

# dicio vazio == dados = {}
'''dados ={1:"Alex",2:"João"}
print (dados[1])'''

'''clientes = []
clientes.append("Alex") #adiciona a lista
clientes.append("João")
clientes.append("Carlos")
clientes.append("Marcos")
clientes.remove("Alex") #remove da lisgta
clientes.insert(0, "Jonas") #insere o nome no indice correspondete
clientes.sort() #ordena a lista
print (clientes)'''

#dicionarios
''''
produto = {}
produto[1] = "Caneta"
produto[2] = "Lápis"
produto[3] = "Borracha"

print(produto)'''

#pessoas={1:"Zezinho",2:"Huguinho",3:"Luizinho"}
#print(list(pessoas))

'''
valores = [1,2]
novo =[]
for i in valores:
    novo.append(1%2)
print(novo)'''

def eh_palindrome(txt):
    for i in range(len(txt)):
        if (txt[i] != txt[len(txt)-i-1]):
            return False
    return   True

inputs = ['arara','elefante','banana','caraarac']
palindromos = list()
for p in inputs:
    if(eh_palindrome(p)):
        palindromos.append(p)
print (palindromos)