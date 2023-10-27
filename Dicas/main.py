###Formatando variáveis no print:

##Incluindo a variável dentro da String:
#print(f"Seu nome é {nome}, sua idade é {idade} e sua nota do semestre passado foi {semestre1}")

##Definindo que a variavel float terá 2 casas decimais:
#print(f"A área do circulo tem {area:,.2f}")

##Fazendo pequenos calculos dentro da propria String:
#print(f"A multiplicação de {numero1} * {numero2} é :  {numero1 * numero2}")

##Criando variavel de texto para diminuir o código:
#texto = '\nO Funcionário {} recebia R${:.2f} e sua Categoria é ({}) portanto seu novo salário é de R${:.2f}'
#print(texto.format(nome,salario,categoria,newsalario))



###Trabalhando com listas:

##Verificando se string informada está na listagem correta:
#categoria5 = {'U', 'V', 'X', 'Y', 'W', 'Z'}
#...
#categoria = input(f"Informe a Categoria do Funcionário : ")
#if categoria in categoria5:
#...

##Criando e printando uma lista de valores em ordem crescente
#lista=[valor1,valor2,valor3]
#print(sorted(lista))



###Trabalhando com Matriz



###Trabalhando com Math
##Tipos de Math e seus Retornos
#import math
#math.ceil(1.001)    # returna 2 
#math.floor(1.001)   # returna 1 
#math.factorial(10)  # returna 3628800
#math.gcd(10,125)    # returna 5 
#math.trunc(1.001)   # returna 1 
#math.trunc(1.999)   # returna 1

###Trabalhando com Numpy
##Tipos de Numpy e seus Retornos
#import numpy
#np.matrix(matriz)   # retorna a matriz de forma gráfica




#marciaww@gmail.com