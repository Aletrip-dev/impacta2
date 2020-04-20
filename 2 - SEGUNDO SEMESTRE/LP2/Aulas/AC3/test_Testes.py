from banco import Cliente, Conta, Banco

c1 = Cliente('Alex',888888,'aletrip@msn.com')
c2= Cliente('Alice',7777777,'alice@alex.com')



b1 = Banco('Banco do Alex')
b1.abre_conta([c1],200)
b1.abre_conta([c2],100)

print('Contas atuais',b1.lista_contas())
print('Nome do banco',b1.get_nome())