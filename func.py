
# exercicio 1
def contaTotal (valorConta):
    gorjeta = (valorConta*10)/100
    total = valorConta +gorjeta
    return total
valorConta= float(input('Digite o valor da conta'))
print(contaTotal(valorConta))


# exercicio 2
def reajuste (nome,salario):
   if (salario>=2000):
       reajustee = '20%'
       r = (salario*20)/100
       valorFinal= salario+r
       return [nome,reajustee,r,valorFinal]
   else:
       reajustee = '15%'
       r = (salario * 15) / 100
       valorFinal = salario + r
       return [nome, reajustee, r, valorFinal]

nome =(input('digite o seu nome'))
salario = float(input('Digite o valor  do seu salario'))
nome, reajustee,r,valorFinal = reajuste(nome,salario)
print('nome do Funcionario', nome)
print('Faixa de reajuste', reajustee)
print('valor do reajuste', r)
print('valor do salario final', valorFinal)

# exercicio 3
def nums (num1, num2):
    soma = num1+num2
    sub = num1+num2
    mut = num1*num2
    div = num1/num2
    return [soma, sub, mut, div]
num1= float(input('Digite o primeiro numero'))
num2= float(input('Digite o segundo numero'))
soma, sub, mut,div =nums(num1,num2)
print('a soma é ',soma)
print('a subtração ',sub)
print('a divisão',div)
print('a multiplicação ',mut)



# exercicio 4
def calcArea(op):
    if(op == 1):
        baseMaior = float(input('Digite a base maior'))
        baseMenor = float(input('Digite a base menor'))
        altura = float(input('Digite a altura'))
        area = ((baseMaior*baseMenor)*altura)/2
        return area
    if(op == 2):
        valorPi=3.14
        raio = float(input('Digite o raio do circulo'))
        area = valorPi * raio**2
        return area
    if(op == 3):
        base = float(input('Digite a base do triangulo'))
        altura = float(input('Digite a altura do triangulo'))
        area = (base*altura)/2
        return area
    if(op == 4):
        base = float(input('Digite a base do retangulo'))
        altura = float(input('Digite a altura do retangulo'))

    if(op == 5):
        diagonalMaior = float(input('Digite a diagonal maior do losangolo'))
        diagonalMenor = float(input('Digite a diagonal menor do losangolo'))
        area = (diagonalMaior*diagonalMenor)/2
        return area
    if(op == 0):
        return 'finalizado!!'

print('1-Calcule a area do trapezio.\n2 - calcule a area do circulo.\n3 - calcule a area do triangulo.\n4 - calcule a area do reatangulo.\n5 - calcule area do losangulo.\n6')
op = int(input('Escolha opção'))
print(calcArea(op))

# exercicio 5

def maiorMenor (num1,num2,num3):
     lista = [num1,num2,num3]
     lista.sort()
     print(lista[0])
     print(lista[2])


maiorMenor(1,5,8)

# exercicio 6
def calcular(estalacao, qtdaconsumida):
    if(estalacao=='R'):
        if(qtdaconsumida<=500):
            valorConta = qtdaconsumida* 0.40
            return valorConta
        else:
            valorConta = qtdaconsumida * 0.65
            return valorConta
    elif(estalacao== 'I'):
        if(qtdaconsumida<=1000):
            valorConta = qtdaconsumida * 0.55
            return valorConta
        else:
            valorConta = qtdaconsumida * 0.60
            return valorConta
    else:
        if(qtdaconsumida<=5000):
            valorConta = qtdaconsumida * 0.55
            return valorConta
        else:
            valorConta = qtdaconsumida * 0.60
            return valorConta

qtdaconsumida = float(input('Digite a quatidade de kwh consumida'))
estalacao = input('Digite seu tipo de estalação(R para residencias, I para industrias e C para comercios')

print(calcular(estalacao,qtdaconsumida))