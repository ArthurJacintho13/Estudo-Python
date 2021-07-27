'''
  Nome : Arthur Barbosa Jacintho Silva
  Descrição: Programa reponsável por:
  - Dado uma palavra, retornar as palavras que diferem dela com uma letra de
    diferença, e essa nova palavra tem de estar presente no arquivo txt 
    "vocabulario.txt"
  - Dado uma palavra de inicio e uma de fim, imprimir uma lista de palavras 
    com o começo sendo a palavra de inicio, as palavras do meio sendo todas as 
    palavras que diferem em uma letra, e por fim a palavra final.
  - Dado uma palavra de inicio e uma de fim, imprimir o caminho de palavras 
    até que chege na palavra final.
'''

def obtemPalavrasProximas(palavra, vocabulario):
    
    palavras_proximas = []

    palavra_aux = palavra

    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # for indo da primeira letra de uma palavra até ultima
    for i in range (len(palavra)):
        # for indo do 'a' até 'z'
        for j in range(len(letras)):
            # concatenando a palavra mudando apenas uma letra de cada vez
            palavra_aux = palavra[:i] + letras[j] + palavra[i+1:]
            if palavra_aux != palavra:
                if palavra_aux in vocabulario:
                    # se a palavra concatenada for diferente da palavra inicial
                    # e se essa palavra estiver no vocabulario, irá adicionar na lista de palavras proximas
                    palavras_proximas.append(palavra_aux)
            palavra_aux = palavra


    
    return palavras_proximas  # lista das palavras próximas


def criaArvoreDeBusca(inicio, fim, vocabulario):

    # Inicializando as listas
    lista_de_lista = []
    lista_palavras = []
    lista_aux = []

    # Adicionando a primeira palavra nas listas
    lista_palavras.append(inicio)
    lista_aux.append(inicio)
    lista_de_lista.append([inicio, -1])

    # Contador
    j = 0
    
    while True: 

        # Caso a ultima palavra da lista for igual a palavra final ou a quantidade de
        # Itens na lista_de_lista for igual a j, o programa irá parar
        if lista_de_lista[len(lista_de_lista)-1][0] == fim or len(lista_de_lista) == j:
            break

        # Associando à lista_palavras o retorno de obtemPalavrasProximas
        # na posicao j
        lista_palavras = obtemPalavrasProximas(lista_de_lista[j][0], vocabulario)

        # For responsavel por ir da posicao inicial de lista_palavra até o final
        # Analisando se a ultima palavra de lista_de_lista é a palavra fim
        # Caso nao seja, irá analisar se as palavras estão na lista_aux, se nao
        # Tiver, irá adicionar na lista_de_lista e na lista_aux.
        for i in range(len(lista_palavras)):
            if lista_de_lista[len(lista_de_lista)-1][0] == fim:
                break
            if lista_palavras[i] not in lista_aux:
                lista_aux.append(lista_palavras[i])
                lista_de_lista.append([lista_palavras[i], j])
        j += 1

    return lista_de_lista  # lista da arvore de busca do caminho
    

def obtemCaminho(inicio, fim, vocabulario):

    # Inicializando as listas
    lista_palavras = []
    lista_aux = []
    lista_aux_palavra = []
    lista_de_lista = []

    # Adicionando a palavra fim em lista_palavras
    lista_palavras.append(fim)

    # Adicionando em lista_de_lista a arvoreDeBusca
    lista_de_lista = criaArvoreDeBusca(inicio, fim, vocabulario)

    # Criando uma lista_aux_palavra com somente as palavras de lista_de_lista
    for i in range(len(lista_de_lista)):
        lista_aux_palavra.append(lista_de_lista[i][0])

    # Contador
    j = 0

    while True:

        # Caso a ultima palavra da lista for igual a palavra inicial ou a quantidade de
        # Itens na lista_de_lista for igual a j, o programa irá parar
        if lista_palavras[len(lista_palavras)-1] == inicio or len(lista_palavras) == j:
            break

        # Associando à lista_aux o retorno de obtemPalavrasProximas
        # na posicao j
        lista_aux = obtemPalavrasProximas(lista_palavras[j], vocabulario)

        # For responsavel por ir da posicao inicial de lista_aux_palavra até o final
        # Analisando se a ultima palavra de lista_palavras é a palavra inicio
        # Caso nao seja, irá analisar se as palavras estão na lista_aux, se
        # Tiver, irá adicionar a primeira palavra na lista_palavras.
        for i in range(len(lista_aux_palavra)):
            if lista_palavras[len(lista_palavras)-1] == inicio:
                break
            if lista_aux_palavra[i] in lista_aux:
                lista_palavras.append(lista_aux_palavra[i])
                break    
        j += 1
  
    return lista_palavras  # lista das palavras do caminho


def main():
    
    # Nome do arquivo de vocabulário
    nome_arquivo = "./vocabulario.txt"

    # Abrindo e associando à vocabulario o arquivo vocabulario.txt
    vocabulario = open(nome_arquivo, 'r')

    # Lendo vocabulario e transformando em uma string unica, depois separando 
    # Em uma lista separada por espaço
    vocabulario = vocabulario.read().split('\n')
    
    # Menu
    while(True):
        opcao = int(input("Digite a opcao: "))

        # Condição de parada
        if opcao == 0:
            break

        # Função 1
        elif opcao == 1:
            palavra = input("Digite uma palavra: ")
            palavras_proximas_2 = []
            palavras_proximas_2 = obtemPalavrasProximas(palavra, vocabulario)     
            print("Palavras proximas de {}: {}".format(palavra, palavras_proximas_2))

        # Função 2
        elif opcao == 2:
            palavra_inicio = input("Digite a palavra de inicio: ")
            palavra_fim = input("Digite a palavra de fim: ")
            arvore = []
            arvore = criaArvoreDeBusca(palavra_inicio, palavra_fim, vocabulario)
            print("Quantidade de nos da arvore: {}".format(len(arvore)))
            print("Arvore: {}".format(arvore))

        # Função 3
        elif opcao == 3:
            palavra_inicio = input("Digite a palavra de inicio: ")
            palavra_fim = input("Digite a palavra de fim: ")
            lista_palavras = obtemCaminho(palavra_inicio, palavra_fim, vocabulario)

            # Se a lista_palavras for igual a um, vai imprimir que nao existe caminho
            if len(lista_palavras) == 1:
                print(f"Nao existe caminho entre {palavra_inicio} e {palavra_fim}")
            else:
                print(f"A distancia entre {palavra_inicio} e {palavra_fim} é {len(lista_palavras)-1}")

                # Como foi feito a lista na ordem ao contrario, pois achei mais
                # Facil encontrar o caminho usando primeiro a palavra fim
                # Logo está sendo printado do ultimo indice da lista até o 
                # primeiro.
                for item in range((len(lista_palavras) -1), -1, -1):
                    if item > 0:

                        # Foi utilizando esse 'end=" "' para que nao pule de linha
                        # Após o print. Foi visto na documentação do python.
                        print(lista_palavras[item], end=" ")
                    else:
                        print(lista_palavras[item])
                    if item > 0:
                        print("->", end=" ")
        

if __name__ == '__main__':
    main()
