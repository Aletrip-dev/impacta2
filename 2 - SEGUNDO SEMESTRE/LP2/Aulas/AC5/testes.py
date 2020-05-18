text = 'testanto@resulta....do'
user = text.split('@')[0]
usuario = text[0]
dominio = text[1]
arrobas = text.count('@')
text = text.replace('@','')
v = text.isalnum()

arrumar = text.translate ({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})

for i in text:
    print (i)
print(arrumar)