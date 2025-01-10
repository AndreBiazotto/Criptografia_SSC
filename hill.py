"""
Cifra de Hill

Esse metodo de encriptação consiste em utilizar uma matriz como chave de criptográfia

Esse códgio atende as requisições da atividade quanto a modo de funcionamento
mas tem uma diferença, pois não solicita um inteiro K e sim uma chave.

Há dois metodos E e D, que recebem X, K e Y e são da seguinte forma:
Y = E(X, K)
X = D(Y, K)
"""
import numpy as np

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def E(texto: str, chave: np.ndarray, tamanho: int) -> str:
    # Verificar se o texto tem tamanho par
    if len(texto) % tamanho != 0:
        texto += "J" * (len(texto) & tamanho)
    texto = texto.upper()
    texto = texto.replace(" ", "")
    
    # Separar o texto em duplas
    texto_formatado = [texto[x:x+tamanho] for x in range(0, len(texto), tamanho)]

    cifra = []
    for texfor in texto_formatado:
        p = [alfabeto.index(t) for t in list(texfor)]
        p_vetor = np.array(p)
        p_vetor = p_vetor.reshape(-1, 1)

        result = np.matmul(chave, p_vetor) % 26

        resultado = result.tolist()

        cifra.append("".join([alfabeto[r[0]] for r in resultado]))
    
    return "".join(cifra)

def D(texto: str, chave: np.ndarray, tamanho: int) -> str:
    det = int(round(np.linalg.det(chave)))  # Determinante da matriz
    det_inv = pow(det, -1, 26)  # Inverso modular do determinante
    adjugate = np.round(det * np.linalg.inv(chave)).astype(int)  # Matriz adjunta
    chave = (det_inv * adjugate) % 26  # Inverso modular da matriz
    print(chave)
    return E(texto, chave, tamanho)


texto = input("Digite um texto para ser processado: ")
tamanho = int(input(f"Digite um tamanho de chave (deve ser menor que {len(texto)}): "))
chave = [i for i in input(f"Escreva uma chave de {tamanho**2} de tamanho (use espaço para separar): ").split()]

matriz = [[0 for _ in range(tamanho)] for __ in range(tamanho)]
for idx_L, linhas in enumerate(matriz):
    for idx_C, coluna in enumerate(linhas):
        matriz[idx_L][idx_C] = int(chave[tamanho * idx_L + idx_C])

matriz_calculo = np.array(matriz)

while np.linalg.det(matriz_calculo) == 0:
    print("Os valores escolhidos não podem ser usados como chave")
    chave = [i for i in input(f"Escreva uma chave de {tamanho**2} de tamanho (use espaço para separar): ").split()]

    matriz = [[0 for _ in range(tamanho)] for __ in range(tamanho)]
    for idx_L, linhas in enumerate(matriz):
        for idx_C, coluna in enumerate(linhas):
            matriz[idx_L][idx_C] = chave[tamanho * idx_L + idx_C]

    matriz_calculo = np.array(matriz)

print(f"Sua chave é:\n{matriz_calculo}")

resposta = int(input("1 - Encripitar\n2 - Desencriptar\nResposta: "))

while (resposta != 1 and resposta != 2):
    print("Inválido!") 
    resposta = int(input("1 - Encripitar\n2 - Desencriptar\nResposta: "))

if resposta == 1:
    print(E(texto, matriz_calculo, tamanho))

if resposta == 2:
    print(D(texto, matriz_calculo, tamanho))
    