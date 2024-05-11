meuDicionario = {'chave01':30, 'chave02':15, 'Texto Puro': 40 ,'chave03':1.5,'chave04':True}
print(meuDicionario)


print(30*'--')
print('')

meuDicionario2 = {'chave01':30 , 'chave02': 'texto puro', 'chave03':1.5 , 'chave03':True}
valorChave02 = meuDicionario2.get('chave02')
print(valorChave02)

meuDicionario2['chave05'] = 2023
meuDicionario2['chave06'] = False
print(meuDicionario2)


print(30*'--')
print('')

dicionarioCores = {}

dicionarioCores['Green']= 'Verde'
dicionarioCores['Black']= 'Preto'
dicionarioCores ['Red']= 'Vermelho'
dicionarioCores ['Blue'] = 'Azul'

print(dicionarioCores)


print(30*'--')
print('')

novoDicionario = {}

for i in range(1,10):
    novoDicionario[i] = i*i

print(novoDicionario)


print(30*'--')
print('')


i =  1
dicionario03 = {}
while i < 5:
    dicionario03[i] = input('Digite um dado para ser adicionado ao dicionario:')
    i+=1
print(dicionario03)

print(30*'--')
print('')

dicionarioCores = {}

dicionarioCores['Green']= 'Verde'
dicionarioCores['Black']= 'Preto'
dicionarioCores ['Red']= 'Vermelho'
dicionarioCores ['Blue'] = 'Azul'


del dicionarioCores ['Red']
print (dicionarioCores)

print(30*'--')
print('')

dicionarioLanguage = {1:'Python', 2:'Java',3:'JavaScript', 4: 'lua', 5: 'Rubi'}
for valor in dicionarioLanguage.values():
     print(valor)
print (30*'#')

print(30*'--')
print('')

for chave in dicionarioLanguage:
     print(chave)
print (30*'#')

for chave, valor in dicionarioLanguage.items():
     print(chave,valor)
print (30*'#')

print(30*'--')
print('')

dicionarioMisto = {1: 2022, 2:2023, 'data': '14/07/1981', 'tupla1':('Ferrari', 'Mercedes','MacLaren'),'lista1':['jan',
                   'fev', 'Mar', 'Abr'], 'status':True, 'tupla2': ('Red bull','willians','Alpine'), 'lista2':['Mai',
                    'Jun', 'Jul', 'Ago','Set'], 'dicionario':{'nome': 'Bob', 'Idade':27, 'Escolaridade': 'Superior Comp.'}}

print(dicionarioMisto)