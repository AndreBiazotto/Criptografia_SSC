"""
Cifra de Cesar (Substituição)
Cada letra será substituida por uma outra, K posições a frente
"""

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def E(p: str, k: int) -> str:
    posicao = (alfabeto.index(p.lower()) + k) % 26
    return alfabeto[posicao]

def D(c: str, k: int) -> str:
    posicao = (alfabeto.index(c.lower()) - k) % 26
    return alfabeto[posicao]

def E_cesar(texto: str, k: int) -> str:
    texto_list = texto.split()
    texto = ""
    for tl in texto_list:
        texto = texto + tl

    cript = ""
    for t in texto:
        cript = cript + E(t, k)

    return cript

def D_cesar(texto: str, k: int) -> str:
    texto_list = texto.split()
    texto = ""
    for tl in texto_list:
        texto = texto + tl

    decript = ""
    for t in texto:
        decript = decript + D(t, k)

    return decript


print(D_cesar(E_cesar("saida pela", 3), 3))