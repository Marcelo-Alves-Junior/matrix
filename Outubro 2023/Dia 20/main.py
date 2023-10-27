import numpy as np

'''Questão 1) Crie um programa que peça 10 números, armazene eles em um vetor e diga qual elemento é o maior, e seu valor e a posição do vetor na qual ele foi armazenado. Para localizar o maior utilize estrutura de decisão. Utilize também uma função do Python para localizar o maior elemento'''

vetor = []
maior, posicao = 0,0

for i in range (10) :
  vetor.append(int(input(f"Informe o número da posição {i} do vetor : ")))

for elemento in range (10) :
  if maior < vetor[elemento] :
    maior = vetor[elemento]
    posicao = elemento

print("\nO maior valor entre os elementos do vetor é o que está na posição {} e seu valor é {} .".format(posicao,maior))


'''Questão 2)  Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida'''

matriz = []

for linha in range (5) :
  matriz.append([])
  for coluna in range (5) :
    if linha == coluna :
      matriz[linha].append(1)
    else :
      matriz[linha].append(0)

print('\n \n')
print(matriz)
print('Inserindo 1 nos elementos da Diagonal Principal e 0 nos demais elementos:\n',np.matrix(matriz))


'''Questão 3) Escreva um algoritmo que preencher uma matriz M(5,5) e calcule as somas:'''
#matriz_exemplo = [ [ 1,2,3,4,5],[7,8,9,11,1],[2,3,4,8,9],[7,4,5,6,3],[2,5,8,9,1] ]

soma_a, soma_b, soma_c, soma_d, soma_e = 0,0,0,0,0
matriz = []

for i in range (5) :
  matriz.append([])
  for j in range (5) :
      matriz[i].append(int(input('Informe um número: ')))

print('Matriz Informada: \n',np.matrix(matriz))

'''a) da linha 4 de M;'''

for i in range (5):
  for j in range (5):
    if i == 3 :
        soma_a = soma_a + matriz[i][j]
print('Questão A: ',soma_a)

'''b) da coluna 2 de M;'''

for i in range (5):
  for j in range (5):
    if j == 1 :
        soma_b = soma_b + matriz[i][j]
print('Questão B: ',soma_b)

'''c) da diagonal principal;'''

for i in range (5):
  for j in range (5):
    if i == j :
        soma_c = soma_c + matriz[i][j]
print('Questão C: ',soma_c)

'''d) da diagonal secundária;'''
# i+j = n+1 NECESSÁRIO FAZER
#https://www.galirows.com.br/meublog/programacao/algoritmo-diagonal-secundaria-matriz/

for i in range (5):
  for j in range (5):
    if i == j :
        soma_d = soma_d + matriz[i][j]
print('Questão D: ',soma_d)

'''e) de todos os elementos da matriz;'''

for i in range (5):
  for j in range (5):
    soma_e = soma_e + matriz[i][j]
print('Questão E: ',soma_e)


'''Questão 4) Escrever um algoritmo que lê um vetor N(20) e o escreve. Troque, a seguir, o 1º elemento com o último, o 2º com o penúltimo etc. até o 10º com o 11º e escreva o vetor N assim modificado.'''

#Criei a variavel remover_elemento para poder remover o elemento do final do vetor que é duplicado ao incluir no ínicio; para o inverso utilizei a própria variavel primeiro_valor. Vetor inicia em 0 e vai até 19, o 20 é o elemento duplicado que deve ser removido

remover_elemento = 20 
vetor = []

for _ in range (20):
  vetor.append(int(input('Informe um número: ')))
print ('Vetor como foi informado: ',vetor)

for primeira_posicao in range (10):
  ultima_posicao = vetor[19 - primeira_posicao]
  vetor.insert(primeira_posicao,ultima_posicao)
  del vetor [remover_elemento]
  vetor.insert(remover_elemento,vetor[primeira_posicao + 1])
  del vetor [primeira_posicao + 1]
  remover_elemento = remover_elemento - 1

print ('Vetor após mudar as posições: ',vetor)