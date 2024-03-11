
print('')
print('1. Apresente o total de itens da lista exibida abaixo com os meses do  ano. Retorno de um número inteiro.')

listaMeses = [ 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho' 
               'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro']

print(len(listaMeses))

print(30* '--')
print( '2. Junte as duas listas em uma terceira lista vazia. Concatene as duas listas.')
print('')

primeiroSemestre = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
segundoSemestre = ['Jun', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

novaLista = primeiroSemestre + segundoSemestre

print(novaLista)

print(30* '--')
print( '3. imprima de maneira separada o primeiro e último iten da lista.')
print('')

listaValores = [2200, 3400, 5750, 800, 2000,1350]

print('Primeiro Valor', listaValores[0])
print('Ultimo Valor', listaValores[-1])

print(30* '--')
print( '4. Adicione o nome Paula Fernandes na posição 2.')
print('')

Nomes = ['Suzy', 'Janaina', 'Claudevan', 'Maria Clara']
print(Nomes)

Nomes.insert(1, 'Paula Fernandes')
print(Nomes)


print(30* '--')
print( '5. Alter o nome Sony para Sony Vaio. Remova o nome Compaq da lista. ')
print('')

Nomes2 = ['Dell', 'Apple', 'Sony', 'Acer','Compaq', 'Positivo','Lenovo']

print(Nomes2)

Nomes2.remove('Compaq')
Nomes2[2] = ('Sony Vaio')
print(Nomes2)

print(30* '--')
print( '6. Imprima em ordem numérica crescente (do menor para o maior) a lista exibida')
print('')

ListaNumeros = [230, 430, 100, 2, 670, 1212, 321, 89, 6, 34, 20,9,99, 710]
ListaNumeros.sort(reverse=False)
print(ListaNumeros)


print(30* '--')
print( '7. Imprima em ordem numérica decrescente (do maior para o menor) a lista exibida abaixo')
print('')

ListaNumeros = [230, 430, 100, 2, 670, 1212, 321, 89, 6, 34, 20,9,99, 710]
ListaNumeros.sort(reverse=True)
print(ListaNumeros)


print(30* '--')
print( '8. Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a soma de todos os números pares da lista. A entrada dos valores deve ser informada pelo usuário.')
print('')

listaI = []
listaPar = []

for i in range (1,10):
    listaI.append(int(input('Digite o valor')))
for i in listaI:
    if i % 2 == 0:
        listaPar.append(i)
print(sum(listaPar));

print(30* '--')
print( '9. Escreva um programa que leia uma lista(10 valores) de números inteiros e imprima a média dos números da lista. Mais uma vez os valores devem ser digitados pelo usuário.')
print('')

listaM  = []
listaMedia = 0

for i in range (1, 10):
    listaM.append(int(input('Digite o numero')))

    listaMedia = (sum(listaM))/10
    print(listaM)
    print('A media é')
    print(listaMedia)




