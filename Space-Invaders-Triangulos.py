'''
  Nome: Arthur Barbosa Jacintho Silva
  Descrição: Programa tendo como base o space invaders, em que os alienigenas são triângulos.
  Sendo assim, para cada alienigena tem que ser dado tres vertices. E assim o programa realiza
  algumas funções, como por exemplo: Quantidade de Pontos na borda de um triangulo; A quantidade
  total de pontos das bordas do triangulo; A quantidade de pontos internos de um treiângulo; A 
  quantidade total de pontos internos nos triângulos; Se um ponto está interno de um triângulo; E
  quais são os limites de busca de um triângulo.
'''

# Função que retorna a distância entre dois pontos
def distanciaDoisPontos (v0, v1):
    return pow((pow((v1[0]-v0[0]), 2) + pow((v1[1]-v0[1]), 2)), 0.5)

# Função que retorna a area de um triangulo - fórmula de Heron
def areaTriangulo (v0, v1, v2):
    semiPerimetro = 0
    ladoA = distanciaDoisPontos(v0, v1)
    ladoB = distanciaDoisPontos(v0, v2)
    ladoC = distanciaDoisPontos(v1, v2)
    semiPerimetro = (ladoA + ladoB + ladoC)/2
    ladoA = semiPerimetro - ladoA
    ladoB = semiPerimetro - ladoB
    ladoC = semiPerimetro - ladoC
    semiPerimetro = semiPerimetro * ladoA * ladoB * ladoC
    semiPerimetro = pow(semiPerimetro, 1/2)
   
    return semiPerimetro


# Subtração Vetores
def subVet (v0, v1):
    v0[0] =  v0[0] - v1[0]
    v0[1] = v0[1] - v1[1]
    return v0

# Função que retorna o valor o determinante da matriz
def det(v0, v1):
    return ((v0[0] * v1[1]) - (v0[1] * v1[0]))

# Funcao que retorna o vertice com o menor valor
def menorVertice(XouY, v0, v1, v2):
    if ((v0[XouY] <= v1[XouY]) and (v1[XouY] <= v2[XouY])):
        return v0[XouY]
    elif ((v0[XouY] <= v2[XouY]) and (v2[XouY] <= v1[XouY])):
        return v0[XouY]
    elif ((v1[XouY] <= v0[XouY]) and (v0[XouY] <= v2[XouY])):
        return v1[XouY]
    elif ((v1[XouY] <= v2[XouY]) and (v2[XouY] <= v0[XouY])):
        return v1[XouY]
    elif ((v2[XouY] <= v0[XouY]) and (v0[XouY] <= v1[XouY])):
        return v2[XouY]
    else:
        return v2[XouY]

# Funcao que retorna o vertice com o maior valor
def maiorVertice(XouY, v0, v1, v2):
    if ((v0[XouY] >= v1[XouY]) and (v1[XouY] >= v2[XouY])):
        return v0[XouY]
    elif ((v0[XouY] >= v2[XouY]) and (v2[XouY] >= v1[XouY])):
        return v0[XouY]
    elif ((v1[XouY] >= v0[XouY]) and (v0[XouY] >= v2[XouY])):
        return v1[XouY]
    elif ((v1[XouY] >= v2[XouY]) and (v2[XouY] >= v0[XouY])):
        return v1[XouY]
    elif ((v2[XouY] >= v0[XouY]) and (v0[XouY] >= v1[XouY])):
        return v2[XouY]
    else:
        return v2[XouY]

# Função MDC de Euclides
def MDC(num1, num2):
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp    
    return num1


# Função que retorna o módulo do número
def abs(num):
    if num < 0:
        return -num
    else:
        return num

# Funcao pra pegar os valores das coordenadas
def leAlienigena(numero_alienigena):
    coordenadas = input("Alienigena %d: " %(numero_alienigena))
    # converte a string lida em uma lista de inteiros
    coordenadas = coordenadas.split()
    for i in range(0,6):
        coordenadas[ i ] = int( coordenadas[ i ] )
    # separa as três coordenadas dos vértices do alienígena
    v0 = [ coordenadas[0], coordenadas[1] ]
    v1 = [ coordenadas[2], coordenadas[3] ]
    v2 = [ coordenadas[4], coordenadas[5] ]
    return v0, v1, v2

# Funcao 1 - Quantidade de pontos na borda
def pontosNaBorda(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    quantidade = 0

    # Entre os pontos v0 e v1
    # paralelo ao eixo x
    if (v0[1] - v1[1] == 0):
        quantidade += abs(v0[0]-v1[0])

    # paralelo ao eixo y
    elif (v0[0] - v1[0] == 0):
        quantidade += abs(v0[1]-v1[1])

    # caso contrario   
    else:
        quantidade += MDC(abs(v0[0]-v1[0]), abs(v0[1]-v1[1]))
    
    # Entre os pontos v0 e v2
    # paralelo ao eixo x
    if (v0[1] - v2[1] == 0):
        quantidade += abs(v0[0]-v2[0])

    # paralelo ao eixo y
    elif (v0[0] - v2[0] == 0):
        quantidade += abs(v0[1]-v2[1])

    # caso contrario   
    else:
        quantidade += MDC(abs(v0[0]-v2[0]), abs(v0[1]-v2[1]))

    # Entre os pontos v1 e v1=2
    # paralelo ao eixo x
    if (v1[1] - v2[1] == 0):
        quantidade += abs(v1[0]-v2[0])

    # paralelo ao eixo y
    elif (v1[0] - v2[0] == 0):
        quantidade += abs(v1[1]-v2[1])

    # caso contrario   
    else:
        quantidade += MDC(abs(v1[0]-v2[0]), abs(v1[1]-v2[1]))

    return quantidade
    

# Funcao 2 - Soma pontos na borda
def somaPontosNaBorda(alienigenas):
    # alienigenas é uma lista de triângulos
    quantidade = 0
    numLista = len(alienigenas)
    for i in range(numLista):
        quantidade += pontosNaBorda(alienigenas[i][0], alienigenas[i][1], alienigenas[i][2])

    return quantidade


# Funcao 3 - Ponto interno
def pontoInterno(ponto, v0, v1, v2):
    # ponto é a coordenada do ponto de uma munição
    x_esta_dentro = (ponto[0] > menorVertice(0, v0, v1, v2)) and (ponto[0] < maiorVertice(0, v0, v1, v2))
    y_esta_dentro = (ponto[1] > menorVertice(1, v0, v1, v2)) and (ponto[1] < maiorVertice(1, v0, v1, v2))
    # se ponto for interno:
    if (x_esta_dentro and y_esta_dentro):
        return True
    # caso contrário:
    else:
        return False

    
# Funcao 4 - Limite de busca
def limitesDeBusca(v0, v1, v2):
  x_min = menorVertice(0, v0, v1, v2)
  y_min = menorVertice(1, v0, v1, v2)
  x_max = maiorVertice(0, v0, v1, v2)
  y_max = maiorVertice(1, v0, v1, v2)
  # v0, v1, v2 são coordenadas dos vértices de um triângulo
  return x_min, y_min, x_max, y_max

# Funcao 5 - Pontos internos
def pontosInternos(v0, v1, v2):
    # v0, v1, v2 são coordenadas dos vértices de um triângulo
    area = areaTriangulo(v0, v1, v2)
    pontosBorda = pontosNaBorda(v0, v1, v2)
    quantidade = (area + 1) - (pontosBorda/2)

    return quantidade



# Funcao 6 - Soma pontos internos
def somaPontosInternos(alienigenas):
    # alienigenas é uma lista de triângulos
    quantidade = 0
    numLista = len(alienigenas)
    for i in range(numLista):
        quantidade += pontosInternos(alienigenas[i][0], alienigenas[i][1], alienigenas[i][2])

    return quantidade

# Codigo para executar os testes:
def main():
    alienigenas = []
    n = int(input("Quantidade de alienigenas: "))
    for i in range(0,n):
        alienigenas.append( leAlienigena(i) )
        
    # Continue aqui o seu programa para testar as funcoes acima...

    Entrada = -1

    while (Entrada != 0):
        Entrada = int(input('Digite a funcao que deseja testar: '))
        if (Entrada == 1):
            Entrada_2 = int(input('Numero do alienigena: '))
            quantidade = pontosNaBorda(alienigenas[Entrada_2][0], alienigenas[Entrada_2][1], alienigenas[Entrada_2][2])
            print('Quantidade de pontos na borda: %d'%quantidade)
        elif (Entrada == 2):
            quantidade = somaPontosNaBorda(alienigenas)
            print('Soma de pontos na borda: %d'%quantidade)
        elif (Entrada == 3):
            ponto = []
            Entrada_3 = int(input('Numero do alienigena: '))
            print(f'Coordenadas do alienigena: {alienigenas[Entrada_3][0]}, {alienigenas[Entrada_3][1]}, {alienigenas[Entrada_3][2]}')
            ponto = input('Coordenadas do ponto: ').split(" ")
            ponto[0] = int(ponto[0])
            ponto[1] = int(ponto[1])
            trueFalse = pontoInterno(ponto, alienigenas[Entrada_3][0], alienigenas[Entrada_3][1], alienigenas[Entrada_3][2])
            if (trueFalse):
                print('Ponto interno ao triangulo!')
            else:
                print('Ponto nao interno ao triangulo!')
        elif (Entrada == 4):
            Entrada_4 = int(input('Numero do alienigena: '))
            x_min, y_min, x_max, y_max = limitesDeBusca(alienigenas[Entrada_4][0], alienigenas[Entrada_4][1], alienigenas[Entrada_4][2])
            print(f'Os limites são: ({x_min},{y_min}) e ({x_max},{y_max})')
        elif (Entrada == 5):
            Entrada_5 = int(input('Numero do alienigena: '))
            quantidade = pontosInternos(alienigenas[Entrada_5][0], alienigenas[Entrada_5][1], alienigenas[Entrada_5][2])
            print('Quantidade de pontos internos: %d'%quantidade)
        elif (Entrada == 6):
            quantidade = somaPontosInternos(alienigenas)
            print('Soma de pontos internos: %d'%quantidade)

    print('ta funcionando tudo')

if __name__ == '__main__':
    main()