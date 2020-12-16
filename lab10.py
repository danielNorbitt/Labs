###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça-Palavras 2.0
# Nome: 
# RA: 
###################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na horizontal (da esquerda para direita) a partir da
posição inicial.  Caso a palavra seja encontrada a partir da posição
inicial a função deve transformar todas as letras da palavra em
maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.
"""
def horizontal(matriz, linha, coluna, palavra):
    if len(palavra) + coluna > len(matriz[-1]):
        return False
    for i in range(len(palavra)):
        if matriz[linha][coluna+i].lower() != palavra[i] and matriz[linha][coluna+i] != "*":
            return False
    for i in range(len(palavra)):
        matriz[linha][coluna+i] = matriz[linha][coluna+i].upper()        
    return True


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na vertical (de cima para baixo) a partir da posição
inicial.  Caso a palavra seja encontrada a partir da posição inicial a
função deve transformar todas as letras da palavra em maiúsculas e
retornar o valor True. Caso contrário, a função de retornar o valor
False.
"""
def vertical(matriz, linha, coluna, palavra):
    if len(palavra) + linha > len(matriz):
        return False
    for i in range(len(palavra)):
        if matriz[linha+i][coluna].lower() != palavra[i] and matriz[linha+i][coluna] != "*":
            return False
    for i in range(len(palavra)):
        matriz[linha+i][coluna] = matriz[linha+i][coluna].upper()        
    return True


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
deve ser buscada na diagonal (no sentido inferior direito) a partir da
posição inicial.  Caso a palavra seja encontrada a partir da posição
inicial a função deve transformar todas as letras da palavra em
maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.
"""
def diagonal1(matriz, linha, coluna, palavra):
    if (len(palavra) + linha > len(matriz)) or len(palavra) + coluna > len(matriz[-1]):
        return False
    for i in range(len(palavra)):
        if matriz[linha+i][coluna+i].lower() != palavra[i] and matriz[linha+i][coluna+i] != "*":
            return False
    for i in range(len(palavra)):
        matriz[linha+i][coluna+i] = matriz[linha+i][coluna+i].upper()        
    return True


"""
Esta função recebe como parâmetro uma matriz, uma posição inicial
na matriz determinada pelos parâmetros linha e coluna e uma palavra
que deve ser buscada na diagonal (sentido superior direito) a partir
da posição inicial.  Caso a palavra seja encontrada a partir da
posição inicial a função deve transformar todas as letras da palavra
em maiúsculas e retornar o valor True. Caso contrário, a função de
retornar o valor False.

"""

def diagonal2(matriz, linha, coluna, palavra):
    if ((linha+1) - len(palavra)) < 0 or len(palavra) + coluna > len(matriz[-1]):
        return False
    for i in range(len(palavra)):
        if matriz[linha-i][coluna+i].lower() != palavra[i] and matriz[linha-i][coluna+i] != "*":
            return False
    for i in range(len(palavra)):
        matriz[linha-i][coluna+i] = matriz[linha-i][coluna+i].upper()        
    return True


# Leitura da matriz

matriz = []
qtdPalavras = 0
palavras = []

while True:
    linha = input()
    if linha.isdigit():
        qtdPalavras = int(linha)
        break
    else:
        matriz.append(linha.split())
for _ in range(qtdPalavras):
    palavra = input()
    palavras.append(palavra)

# Dica: use linha.isdigit(), linha.split() e matriz.append()
# para processar a entrada e armazenar a matriz de caracteeres



# Leitura e processamento das palavras



print("-" * 40)
print("Lista de Palavras")
print("-" * 40)
for palavra in palavras:
    ocorrencias = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[-1])):
            if horizontal(matriz,i,j,palavra):
                ocorrencias += 1
            if vertical(matriz,i,j,palavra):
                ocorrencias += 1
            if diagonal1(matriz,i,j,palavra):
                ocorrencias += 1
            if diagonal2(matriz,i,j,palavra):
                ocorrencias += 1
    print("Palavra:", palavra)
    print("Ocorrencias:", ocorrencias)
    print("-" * 40)

# Impressão da matriz

for linha in matriz:
  print(" ".join(linha))