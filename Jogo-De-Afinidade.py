"""
  Nome: Arthur Barbosa Jacintho Silva
  Descrição: Exercicio em que não podia utilizar funções, e é responsável por: 
  - Dado dois numeros, terá de descobrir a afinidade entre eles. Do primeiro modo, 
  será somado todos os algoritmos de cada número até que ele tenha apenas um algotimo cada. 
  Após isso a afinidade é a divisão de um pelo outro. Caso você queira jogada aleatórias 
  o prgrama simulará 10000 partidas com números aleatórios.
"""

## parâmetros para o método das congruências lineares:
m = 2**32
a = 22695477
c = 1
numero_aleatorio_anterior = 42
numAcertos = 0
qnt_Vezes_Maior = 0

numJogadas = int(input("Digite o numero de jogadas: "))
for x in range (numJogadas):
  n1 = int(input("Pessoa 1: digite um numero: "))
  n2 = int(input("Pessoa 2: digite um numero: "))
  soma_n1 = 0
  soma_n2 = 0
  resto_n1 = 0
  resto_n2 = 0
  while (n1 != 0):
    resto_n1 = n1 % 10
    n1 = (n1 - resto_n1)//10
    soma_n1 = soma_n1 + resto_n1
    if (n1 == 0 and soma_n1 > 9):
      n1 = soma_n1
      soma_n1 = 0
  while (n2 != 0):
    resto_n2 = n2 % 10
    n2 = (n2 - resto_n2)//10
    soma_n2 = soma_n2 + resto_n2
    if (n2 == 0 and soma_n2 > 9):
      n2 = soma_n2
      soma_n2 = 0
  if (soma_n1 == soma_n2):
    numAcertos = numAcertos + 1

qrAleatorio = input("Deseja simular jogadas aleatorias (S/N)? ")

if (qrAleatorio == 'S' and numAcertos != 0):
  for p in range(10000):
    numAcertos_linha = 0
    for s in range(numJogadas):      
      n1_linha = (a * numero_aleatorio_anterior + c) % m
      numero_aleatorio_anterior = n1_linha
      n2_linha = (a * numero_aleatorio_anterior + c) % m
      numero_aleatorio_anterior = n2_linha
      soma_n1_linha = 0
      soma_n2_linha = 0
      resto_n1_linha = 0
      resto_n2_linha = 0
      while (n1_linha != 0):
        resto_n1_linha = n1_linha % 10
        n1_linha = (n1_linha - resto_n1_linha)//10
        soma_n1_linha = soma_n1_linha + resto_n1_linha
        if (n1_linha == 0 and soma_n1_linha > 9):
          n1_linha = soma_n1_linha
          soma_n1_linha = 0
      while (n2_linha != 0):
        resto_n2_linha = n2_linha % 10
        n2_linha = (n2_linha - resto_n2_linha)//10
        soma_n2_linha = soma_n2_linha + resto_n2_linha
        if (n2_linha == 0 and soma_n2_linha > 9):
          n2_linha = soma_n2_linha
          soma_n2_linha = 0
      if (soma_n1_linha == soma_n2_linha):
        numAcertos_linha = numAcertos_linha + 1
    if (numAcertos_linha >= numAcertos):
      qnt_Vezes_Maior = qnt_Vezes_Maior + 1

  
  p = qnt_Vezes_Maior / 10000
  afinidade = 1 - p

  print("A afinidade de voces e de {afinidade}")
  if (afinidade >= 0 and afinidade < 1/3):
    print("A afinidade de voces e baixa. Que pena!")
  elif (afinidade >= 1/3 and afinidade < 2/3):
    print("A afinidade de voces e mediana!")
  else:
    print("Parabens! Voces tem uma bela afinidade!”")
else:
  afinidade = numAcertos/numJogadas
  print("A afinidade de voces e de {afinidade}")
  if (afinidade >= 0 and afinidade < 1/3):
    print("A afinidade de voces e baixa. Que pena!")
  elif (afinidade >= 1/3 and afinidade < 2/3):
    print("A afinidade de voces e mediana!")
  else:
    print("Parabens! Voces tem uma bela afinidade!”")

