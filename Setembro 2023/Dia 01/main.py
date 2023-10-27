import math

func = funcoes

##Arquivo: Lista_Aula_01

# 1 – Faça um programa que calcula a área de um círculo, tendo como entrada o raio do mesmo.

pi = 3.14159265359
raio = float (input("Informe o valor do raio do círculo: "))
area = pi * (raio**2)
print(f"A área do circulo tem {area:,.2f}")


# 2	– Faça um programa que multiplique dois números inteiros e mostre o resultado da multiplicação

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
print(f"A multiplicação de {numero1} * {numero2} é :  {numero1 * numero2}")


# 3 - Faça um programa que calcule a área de triângulo equilátero (todos os lados são iguais), tendo como entrada a base e a altura.")

base = float(input("Informe a base do triângulo equilátero: "))
altura = float(input("Informe a altura do triângulo equilátero: "))
area = (base*altura) / 2
print(f"A área de triângulo equilátero é {area}")


# 4 – Faça um programa que calcule e exiba a média de dois números digitados.")

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
media = (numero1 + numero2) / 2
print(f"A média entre os números {numero1} e {numero2} é: {media:,.2f}")


# 5 – Faça um programa que leia a temperatura em graus Celsius e apresente convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C + 160)/5. Sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

celsius = float(input("Informe a temperatura em graus Celsius: "))
fahrenheit = ((9*celsius)/5)+(160/5)
print(f"A temperatura em graus Fahrenheit é de: {fahrenheit} ")


# 6 – Efetuar a leitura de um número inteiro e apresentar a raiz quadrada deste número.")

numero = float (input("Informe um número; iremos calcular sua raiz quadrada :"))
raiz = numero**0.5
print(f"O valor da raiz quadrada de {numero:.0f} é {raiz:.0f}")


# 7 – Elaborar um programa que calcule e apresente o volume de uma caixa retangular, por meio da fórmula: volume = comprimento * largura * altura")

comprimento = float (input("Informe o comprimento da caixa em centímetros (cm); \niremos calcular o volume da caixa em metros cúbicos (m³) : "))
largura = float (input("Informe a largura da caixa em centímetros (cm); \niremos calcular o volume da caixa em metros cúbicos (m³) : "))
altura = float (input("Iremos calcular o volume da caixa em metros cúbicos (m³) Informe a altura da caixa em centímetros (cm): "))
volume = (comprimento/100)*(largura/100)*(altura/100)
print(f"Uma caixa com {comprimento:.0f}cm de comprimento, {largura:.0f}cm de altura e {altura:.0f}cm de altura; tem {volume}m³ de volume")


# 8 – Ler dois valores inteiros para as variáveis A e B. Efetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.")

variavelA = float(input("Informe o valor da variável A: "))
variavelB = float(input("Informe o valor da variável B: "))
print(f"O valor variável A é: {variavelA} e da variável B é: {variavelB}")
variaveltemporaria = variavelA
variavelA = variavelB
variavelB = variaveltemporaria
print("Invertendo valores ... ")
print(f"O novo valor variável A é: {variavelA} e da variável B é: {variavelB}")


# 9 - Construa um programa que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos de combustível, onde são fornecidos a altura e o raio desse cilindro. Sabendo que:

precoDaLata = 20 # A lata de tinta custa R$20,00
litrosPorLata = 5 # Cada lata contém 5 litros 
metrosPorLitro = 3 # Cada litro de tinta pinta 3 metros quadrados. 
areaCilindro=(2*3.14*(raio**2)) + (2*3.14*raio*altura) # Área do cilindro=2*3.14*raio² + 2*3.14*raio*altura 
# E que raio e altura são dados de entrada.

raio = float(input("Informe o raio do cilindro: "))
altura = float(input("Informe a altura do cilindro: "))
metrosPorLata = litrosPorLata * metrosPorLitro
latasPorCilindro = areaCilindro / metrosPorLata
print(f"Será necessário {latasPorCilindro:.3f} latas para pintar o Cilindro de {areaCilindro} m²")
custo = (math.ceil(latasPorCilindro))*precoDaLata
print(f"O custo total será: R${custo:.2f}")


# 10 - Construa um programa que tendo como entrada dois pontos quaisquer do plano P(x1,y1) e Q(x2,y2), imprima a distância entre eles.

x1 = float (input("Digite o valor de x1: "))
y1 = float (input("Digite o valor de y1: "))
x2 = float (input("Digite o valor de x2: "))
y2 = float (input("Digite o valor de y2: "))
print(f"Os valores dos pontos do plano P: (x1= {x1:.2f}, y1= {y1:.2f}) e Q: (x2= {x2:.2f}, y2= {y2:.2f})")
formula = ((((x2-x1)**2)+((y2-y1)**2))*0.5)
print(f"A distancia entre os pontos do plano P e Q é: {formula:.2f}")


# 11 – Construir um programa que efetue o cálculo do salário líquido de um funcionário. Para fazer este programa, você deve possuir alguns dados, tais como: valor da hora, número de horas trabalhadas no mês e percentual de desconto do INSS. Em primeiro lugar, deve-se estabelecer qual será o seu salário bruto para efetuar o desconto e ter o valor do salário líquido.

valorDaHora = float (input("Informe o valor da hora trabalhada: "))
horasPorMes = float (input("Informe a quantidade de horas trabalhadas: "))
salario = valorDaHora * horasPorMes
print(f"Salário: {salario}")
aliquota1 = 1320 * 0.075
aliquota2 = (2571.29 - 1320) * 0.09
aliquota3 = (3856.94 - 2571.29) * 0.12
if salario <= 1320 :
  descontoInss = salario * 0.075
elif salario <= 2571.29 :
  descontoInss = ((salario - 1320.00) * 0.09) + aliquota1
elif salario <= 3856.94 :
  descontoInss = ((salario - 2571.29) * 0.12) + aliquota2 + aliquota1
else:
  descontoInss = ((salario - 3856.94) * 0.14) + aliquota3 + aliquota2 + aliquota1
salarioLiquido = salario - descontoInss
print(f"O valor do Salário Líquido é de: {salarioLiquido:.2f}")


# 12 - Faça um algoritmo que leia dois números A e B e mostre o maior deles.

a = float (input("Digite o valor de A: "))
b = float (input("Digite o valor de B: "))
if a>b :
  print(f"O valor de A ({a}) é maior que o valor de B ({b})")
elif a<b :
  print(f"O valor de B ({b}) é maior que o valor de A ({a})")
else:
  print(f"O valor de A ({a}) é IGUAL ao valor de B ({b})")


# 13 - Faça um algoritmo que leia um número N e mostre “F1”, “F2” ou “F3”, conforme a condição:
# “F1”, se N <= 10 
# “F2”, se N > 10 e N <= 100 
# “F3”, se n > 100

n = float (input("Digite o valor de N: "))
if n<=10 :
  print("F1")
elif n<=100 :
  print("F2")
else:
  print("F3")


# 14 -  O sistema de avaliação de determinada disciplina, é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Faça um algoritmo para calcular a média final de um aluno desta disciplina.

prova1 = float (input("Informe a nota da primeira prova: "))
prova2 = float (input("Informe a nota da segunda prova: "))
prova3 = float (input("Informe a nota da terceira prova: "))
media = ((prova1*2) + (prova2*3) + (prova3*5)) / 10
print(f"A média final do aluno é {media:.2f}")


# 15 - Construa um algoritmo que receba como entrada três valores e os mostre em ordem crescente.

valor1 = float (input("Informe o primeiro valor: "))
valor2 = float (input("Informe o segundo valor: "))
valor3 = float (input("Informe o terceiro valor: "))

if valor1>=valor2 and valor2>valor3 :
  print (valor3,valor2,valor1)
elif valor1>=valor2 and valor2<valor3 :
  print(valor2,valor1,valor3)
elif valor1<valor2 and valor2<=valor3 :
  print (valor1,valor2,valor3)


# 16 - Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. Considerando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, construa um algoritmo que forneça:
# a) o nome e as notas em cada prova do candidato
# b) a média do candidato
# c) uma informação dizendo se o candidato foi aprovado ou não.
# Considere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0")

menor_nota = 0
aprovado = 'Sim'
nome = input("Informe o Nome do aluno: ")
pt = float(input(f"Informe a nota de Portugues do {nome}: "))
mat = float(input(f"Informe a nota de Matemática do {nome}: "))
con = float(input(f"Informe a nota de Conhecimentos Gerais do {nome}: "))

media = (pt + mat + con) / 3

if pt >= mat and mat <= con:
  menor_nota = mat
elif pt <= con:
  menor_nota = pt
else:
  menor_nota = con

if menor_nota < 5 or media < 7:
  aprovado = 'Reprovado'
else:
  aprovado = 'Aprovado'

print(f"O aluno {nome} tirou em Portugues {pt:,.2f} Matemática {mat:,.2f} Conhecimentos Gerais {con:,.2f} \nSua média foi {media:,.2f} , sua menor nota foi {menor_nota:,.2f} portanto ele foi {aprovado}")


# 17 - Uma empresa irá dar um aumento de salário aos seus funcionários de acordo com a categoria de cada empregado. O aumento seguirá a seguinte regra: Funcionários das categorias A, C, F, e H ganharão 10% de aumento sobre o salário; Funcionários das categorias B, D, E, I, J e T ganharão 15% de aumento sobre o salário; \nFuncionários das categorias K e R ganharão 25% de aumento sobre o salário; \nFuncionários das categorias L, M, N, O, P, Q e S ganharão 35% de aumento sobre o salário; \nFuncionários das categorias U, V, X, Y, W e Z ganharão 50% de aumento sobre o salário. \nFaça um algoritmo que mostre nome, categoria e salário reajustado de cada empregado.\n")

categoria1 = {'A', 'C', 'F','H'}
categoria2 = {'B', 'D', 'E', 'I', 'J', 'T'}
categoria3 = {'K','R'}
categoria4 = {'L', 'M', 'N', 'O', 'P', 'Q', 'S'}
categoria5 = {'U', 'V', 'X', 'Y', 'W', 'Z'}
nome = input("Informe o nome do Funcionário: ")
salario = float (input(f"Informe o salário do Funcionário : "))
categoria = input(f"Informe a Categoria do Funcionário : ")
texto = '\nO Funcionário {} recebia R${:.2f} e sua Categoria é ({}) portanto seu novo salário é de R${:.2f}'
if categoria in categoria1:
  newsalario = salario + (salario * 0.1)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria2:
  newsalario = salario + (salario * 0.15)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria3:
  newsalario = salario + (salario * 0.25)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria4:
  newsalario = salario + (salario * 0.35)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria5:
  newsalario = salario + (salario * 0.5)
  print(texto.format(nome,salario,categoria,newsalario))
else:
  print("Categoria informada não existe")