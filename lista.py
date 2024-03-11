#Criar lista

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = [1, 2, 'Junior', 'Aline', 4, 4.5]

print(lista1)
print(30* '--')  #para dar espaço
print(lista2)


#Inserir dado, por ultimo

lista2.append('Allan')
print(lista2)

print(30* "--") #para dar espaço

#inserir por colocação que desejar (no insert num posição e o nome que deseja )

nomes = ['Paula', 'Mariana', 'Giovanna', 'Paschoal']
print(nomes)

nomes.insert(0, 'Ana')
print(nomes)

#Update da lista (atualizar item tres/ ou item q quiser)

print(30* "--")

linguagens = ['Python', 'Java', 'JavaScript', 'C']
print(linguagens)

linguagens[3] = ['Ruby']
print(linguagens)

#Delete ( remover um dado )

print(30* "--")
lista3 = [1, 2, 'Junior', 'Aline', 4, 4.5]
print(lista3)

lista3.remove('Junior')
print(lista3)




