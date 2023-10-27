print("1 - Faça um algoritmo que soma os números de 1 a 100 e exibe resultado da soma")

i = 1
soma = 0
while i <=100 :
  soma = soma + i
  i = i + 1
print (soma)


print("2 - Construa um Algoritmo que, para um grupo de 50 valores inteiros, determine: \na) A soma dos números positivos; \nb) A quantidade de valores negativos\n")

negativo = 0
positivo = 0
for _ in range (5):
  valor = int(input("Informe um valor: "))
  if valor >=0:
    positivo = positivo + valor    
  else:
    negativo = negativo + 1    
print ("A soma dos positivos é {} e a quantidade de negativos é {}".format(positivo,negativo))


print("3 - Faça um algoritmo que imprima os múltiplos positivos de 7, inferiores a 1000.")

a = 7
i = 0
while (i + 7) <1000 :
  i = i + 7
  print(i)


print("4 - Faça um algoritmo que calcule o valor de A, dado por:")

denominador = 1
numerador = 0
a=0
n = int(input("Informe um número: "))
while numerador < n :
  a = a + ((n-numerador)/denominador)
  print(a)
  numerador = numerador + 1
  denominador = denominador + 1
print(a)


print("5 - Faça um algoritmo que calcule a média de salários de uma empresa, pedindo ao usuário a quantidade de funcionários, o nome e o salário de cada funcionário e devolvendo a média, o salário mais alto e o salário mais baixo")

maior = 0
menor = 0
totalsalario = 0
qtfun = int(input("Informe a quantidade de Funcionários :"))
for _ in range (qtfun):
  salario = float (input("Informe o salario do Funcionário :"))  
  totalsalario = totalsalario + salario
  if maior < salario:
    maior = salario
  if menor > salario or menor==0:
    menor = salario
media = totalsalario / qtfun  
print(media,maior,menor)

print("6 - Escreva um algoritmo que determine o fatorial de um número. Para este problema, tem-se como entrada o valor do número do qual se deseja calcular o fatorial. O fatorial de 0 é igual a 1. O fatorial de um número N(N!) é definido conforme a seguir")

n = int (input("Informe um número:"))
#MODO 1
fat = 1
i = 0
while i < n:
  fat = fat * (n - i)
  i = i + 1
print (fat)

#MODO 2
fat = n
i = 1
while i < n:
  fat = fat * (n - i)
  i = i + 1
print (fat)


print("7 - Sem utilizar a operação de multiplicação, escreva um programa que multiplique dois números inteiros. Por exemplo: 2 * 2 = 2 + 2.")

contador = 1
mult = 0
n1 = int (input("Informe um número:"))
n2 = int (input("Informe outro número:"))
while contador <= n1 :
  mult = mult + n2
  contador = contador + 1
print(mult)


print("8 - A série de Fibonacci é formada pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... Construa um algoritmo que gere e mostre a série até o vigésimo termo.")

termo, ultimo = 0,0
penultimo, i = 1,1
while i <= 20:
  print(termo)
  termo = ultimo + penultimo
  penultimo = ultimo
  ultimo = termo
  i = i + 1

print("9 - Faça um algoritmo que leia um conjunto de números (X) e imprima sua soma (Soma) e sua média (Media). Admita que o valor 9999 é utilizado como sentinela para fim de leitura. Ex.: 1, 2, 3 => Soma=6 Media=2")
i = 1
soma = 0
n1 = int (input("Informe a quantidade de números :"))
while i <= n1 :
  numero = int (input(f"Informe o {i}º número :"))
  soma = soma + numero
  i = i + 1
media = soma / n1
print("A soma dos números é {:.0f} e a média dos valores é {:.2f}".format(soma,media))
#Precisa validar o sentinela


print("10 - Escrever um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o valor de E. E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!") 

fat = n
i = 1
while i < n:
  fat = fat * (n - i)
  i = i + 1
print (fat)

#Precisa Completar