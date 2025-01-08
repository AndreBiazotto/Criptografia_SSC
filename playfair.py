"""
Esse códgio atende as requisições da atividade quanto a modo de funcionamento
mas tem uma diferença, pois não solicita um inteiro K e sim uma chave.

Há dois metodos E e D, que recebem X, K e Y e são da seguinte forma:
Y = E(X, K)
X = D(Y, K)

Metodos adicionais são necessários para melhor compreenção do algorimo.
"""

alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def E(x: str, k: str) -> str:
    k = k.upper()
    k.replace(" ", "")                   # Remove estaços em branco
    list_K = list(k)                     # Transforma em lista
    list_K = list(dict.fromkeys(list_K)) # Remode duplicadas            

    # PRIMEIRO PASSO: criar a matriz de encripitação
    matriz_playfair = [["0" for __ in range(5)] for _ in range(5)]

    alfabeto_list = list(alfabeto)
    alfabeto_list = [l for l in alfabeto_list if l not in list_K] # Remove as letras da chave

    alfabeto_matriz = list_K + alfabeto_list # Concatenar

    # Cada letra é alocada em uma posição na matriz
    for index_linha, linha in enumerate(matriz_playfair):
        for index_coluna, __ in enumerate(linha):
            matriz_playfair[index_linha][index_coluna] = alfabeto_matriz[index_linha * 5 + index_coluna]

    # SEGUNDO PASSO: formatar a mensagem
    x = x.upper()
    x = x.replace(" ", "")
    sinais_graficos_cedilha = ["Á", "É", "Í", "Ó", "Ú", "Ã", "Õ", "Ç"]
    trocas = ["A", "E", "I", "O", "U", "A", "O", "C"]
    for inx, sgc in enumerate(sinais_graficos_cedilha):
        x = x.replace(sgc, trocas[inx])
    list_X = list(x)

    # Adicionar uma letra caso exista repetição de letra
    for lx in range(len(list_X) - 1):
        if list_X[lx] == list_X[lx + 1]:
            list_X = list_X[:lx + 1] + ["X"] + list_X[lx + 1:]

    if len(list_X) % 2 != 0:
        list_X += ["Z"]

    # Organiza as letras em pares
    list_X_pares = []
    for lx in range(0, len(list_X) - 1, 2): 
        list_X_pares.append(list_X[lx] + list_X[lx + 1])

    # TERCEIRO PASSO: cifragem
    list_Y = []
    for pares in list_X_pares:
        pri = [(index, row.index(pares[0])) for index, row in enumerate(matriz_playfair) if pares[0] in row]
        sec = [(index, row.index(pares[1])) for index, row in enumerate(matriz_playfair) if pares[1] in row]

        pri_cod = ""
        sec_cod = ""

        # REGRA DA LINHA
        if pri[0][0] == sec[0][0]:
            if pri[0][1] == 4:
                pri_cod = matriz_playfair[pri[0][0]][0]
            else:
                pri_cod = matriz_playfair[pri[0][0]][pri[0][1] + 1]
            if sec[0][1] == 4:
                sec_cod = matriz_playfair[sec[0][0]][0]
            else:
                sec_cod = matriz_playfair[sec[0][0]][sec[0][1] + 1]

        # REGRA DA COLUNA
        if pri[0][1] == sec[0][1]:
            if pri[0][0] == 4:
                pri_cod = matriz_playfair[0][pri[0][1]]
            else:
                pri_cod = matriz_playfair[pri[0][0] + 1][pri[0][1]]
            if sec[0][0] == 4:
                sec_cod = matriz_playfair[0][sec[0][1]]
            else:
                sec_cod = matriz_playfair[sec[0][0] + 1][sec[0][1]]
        
        if pri[0][0] != sec[0][0] and pri[0][1] != sec[0][1]:
            pri_cod = matriz_playfair[pri[0][0]][sec[0][1]]
            sec_cod = matriz_playfair[sec[0][0]][pri[0][1]]

        list_Y.append(pri_cod + sec_cod)

    return "".join(list_Y)
        

def D(y: str, k: str) -> str:
    k = k.upper()
    k.replace(" ", "")                   # Remove estaços em branco
    list_K = list(k)                     # Transforma em lista
    list_K = list(dict.fromkeys(list_K)) # Remode duplicadas   

    # PRIMEIRO PASSO: criar a matriz de encripitação
    matriz_playfair = [["0" for __ in range(5)] for _ in range(5)]

    alfabeto_list = list(alfabeto)
    alfabeto_list = [l for l in alfabeto_list if l not in list_K] # Remove as letras da chave

    alfabeto_matriz = list_K + alfabeto_list # Concatenar

    # Cada letra é alocada em uma posição na matriz
    for index_linha, linha in enumerate(matriz_playfair):
        for index_coluna, __ in enumerate(linha):
            matriz_playfair[index_linha][index_coluna] = alfabeto_matriz[index_linha * 5 + index_coluna]

    # SEGUNDO PASSO: formatar a mensagem
    y = y.upper()
    y = y.replace(" ", "")
    sinais_graficos_cedilha = ["Á", "É", "Í", "Ó", "Ú", "Ã", "Õ", "Ç"]
    trocas = ["A", "E", "I", "O", "U", "A", "O", "C"]
    for inx, sgc in enumerate(sinais_graficos_cedilha):
        y = y.replace(sgc, trocas[inx])
    list_Y = list(y)

    if len(list_Y) % 2 != 0:
        list_Y += ["Z"]

    # Organiza as letras em pares
    list_Y_pares = []
    for ly in range(0, len(list_Y) - 1, 2): 
        list_Y_pares.append(list_Y[ly] + list_Y[ly + 1])

    # TERCEIRO PASSO: cifragem
    list_X = []
    for pares in list_Y_pares:
        pri = [(index, row.index(pares[0])) for index, row in enumerate(matriz_playfair) if pares[0] in row]
        sec = [(index, row.index(pares[1])) for index, row in enumerate(matriz_playfair) if pares[1] in row]

        pri_cod = ""
        sec_cod = ""

        # REGRA DA LINHA
        if pri[0][0] == sec[0][0]:
            if pri[0][1] == 0:
                pri_cod = matriz_playfair[pri[0][0]][4]
            else:
                pri_cod = matriz_playfair[pri[0][0]][pri[0][1] - 1]
            if sec[0][1] == 0:
                sec_cod = matriz_playfair[sec[0][0]][4]
            else:
                sec_cod = matriz_playfair[sec[0][0]][sec[0][1] - 1]

        # REGRA DA COLUNA
        if pri[0][1] == sec[0][1]:
            if pri[0][0] == 0:
                pri_cod = matriz_playfair[4][pri[0][1]]
            else:
                pri_cod = matriz_playfair[pri[0][0] - 1][pri[0][1]]
            if sec[0][0] == 0:
                sec_cod = matriz_playfair[4][sec[0][1]]
            else:
                sec_cod = matriz_playfair[sec[0][0] - 1][sec[0][1]]
        
        if pri[0][0] != sec[0][0] and pri[0][1] != sec[0][1]:
            pri_cod = matriz_playfair[pri[0][0]][sec[0][1]]
            sec_cod = matriz_playfair[sec[0][0]][pri[0][1]]

        list_X.append(pri_cod + sec_cod)

    return "".join(list_X)

    

texto = input("Digite um texto para ser processado: ")
chave = input("Escreva uma chave: ")

resposta = int(input("1 - Encripitar\n2 - Desencriptar\nResposta: "))

while (resposta != 1 and resposta != 2):
    print("Inválido!") 
    resposta = int(input("1 - Encripitar\n2 - Desencriptar\nResposta: "))

if resposta == 1:
    print(E(texto, chave))

if resposta == 2:
    print(D(texto, chave))
    