#Função

# Criar algumas funções e utiliza-las depois

#Função de Soma de 3 variaveis:
def somando (a,b,c):
  soma = a + b + c
  return soma

#Função de Média de 3 variaveis:
def tirando_media (x,y,z):
  media = (x + y + z) / 3
  return media

#Executando função

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

print("A média dos tres números é: ", tirando_media(a, b, c))
print("A soma dos tres números é: ", somando(a, b, c))
