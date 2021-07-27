"""
  Nome: Arthur Barbosa Jacintho Silva
  Descrição: Exercicio em que não podia utilizar funções, e é responsável por: 
  - Simular um jogo de adivinhação, com a semente sendo recebida pelo teclado. O 
  programa diz quando chutou alto, e da dica para tentar par ou impar. Ele se 
  encerra quando as tentativas se encerram ou quando acerta a palavra.
"""

import random

# lendo a semente da funcao random
semente = int(input("Digite a semente do sorteio: "))

# Criando a semente
random.seed(semente)

# Criando o numero pseudo-aleatorio num intervalo de 1 ate 20
numero_sorteado = random.randint(1,20)

print("Escolhi um inteiro entre 1 e 20. Adivinhe-o!")

# Variavel responsavel por contar as tentativas
count = 0

# Variavel responsavel por armazenar as tentativas do usuario
Numero = 0

# Laco de repeticao com argumento de parada sendo count = 6, tendo em vista
# que nao podemos usar break nesse exercicio
while (count != 6):

  # Lendo o numero de entrada do usuario
  Numero = int(input())
  count = count + 1
  print(f"Seu chute: {Numero}")

  # Condicoes para que, caso o Numero de entrada seja maior que o numero sortado
  # ira falar que chutou alto, e caso o numero sorteado seja par, pedira para
  # o usuario chutar um numero impar ou o contrario
  if (Numero > numero_sorteado):
    print("Chutou alto")
    if (numero_sorteado % 2 == 0):
      if (Numero % 2 == 1):
        print("Tente um par")
    else:
      if (Numero % 2 == 0):
        print("Tente um impar")

  # Condicoes para que, caso o Numero de entrada seja menor que o numero sortado
  # ira falar que chutou baixo, e caso o numero sorteado seja par, pedira para
  # o usuario chutar um numero impar ou o contrario
  elif (Numero < numero_sorteado):
    print("Chutou baixo")
    if (numero_sorteado % 2 == 0):
      if (Numero % 2 == 1):
        print("Tente um par")
    else:
      if (Numero % 2 == 0):
        print("Tente um impar")

  # Condicao de que o usuario acertou o numero
  else:
    print(f"Legal, acertou na tentativa {count}")

    # Como nao podemos usar break, como essa seria um lugar para por o break
    # associei count ao valor de parada do while
    count = 6
  if (count == 5):
    print(f"Tentativas esgotadas!\nO escolhido foi o {numero_sorteado}")
    
    # Como nao podemos usar break, como essa seria um lugar para por o break
    # associei count ao valor de parada do while
    count = 6




