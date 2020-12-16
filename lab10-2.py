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
    tamanhoP = len(palavra)
    if tamanhoP + coluna > len(matriz[-1]):
        return False
    for letra in range(tamanhoP):
        if matriz[linha][coluna+letra].lower() != palavra[letra] and matriz[linha][coluna+letra] != "*":
            return False
    for letra in range(tamanhoP):
        toUpper(matriz,linha,coluna+letra)        
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
    tamanhoP = len(palavra)
    if tamanhoP + linha > len(matriz):
        return False
    for letra in range(tamanhoP):
        if matriz[linha+letra][coluna].lower() != palavra[letra] and matriz[linha+letra][coluna] != "*":
            return False
    for letra in range(tamanhoP):
        toUpper(matriz,linha+letra,coluna)    
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
    tamanhoP = len(palavra)
    if (tamanhoP + linha > tamanhoP) or tamanhoP+ coluna > len(matriz[0]):
        return False
    for letra in range(tamanhoP):
        if matriz[linha+letra][coluna+letra].lower() != palavra[letra] and matriz[linha+letra][coluna+letra] != "*":
            return False
    for letra in range(tamanhoP):
        toUpper(matriz,linha+letra,coluna+letra)  
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
    tamanhoP = len(palavra)
    if ((linha+1) - tamanhoP) < 0 or tamanhoP + coluna > len(matriz[0]):
        return False
    for letra in range(tamanhoP):
        if matriz[linha-letra][coluna+letra].lower() != palavra[letra] and matriz[linha-letra][coluna+letra] != "*":
            return False
    for letra in range(tamanhoP):
        toUpper(matriz,linha-letra,coluna+letra)  
    return True

def toUpper(matriz,linha,coluna):
    matriz[linha][coluna] = matriz[linha][coluna].upper()  

# Leitura da matriz

matriz = []
qtdP = 0
palavras = []
parada = True

while parada:
    linha = input()
    if linha.isdigit():
        qtdP = int(linha)
        parada = False
    else:
        linha = linha.split()
        matriz.append(linha)

for i in range(qtdP):
    palavra = input()
    palavras.append(palavra)

# Dica: use linha.isdigit(), linha.split() e matriz.append()
# para processar a entrada e armazenar a matriz de caracteeres



# Leitura e processamento das palavras



print("-" * 40)
print("Lista de Palavras")
print("-" * 40)
for palavra in palavras:
    ocorrencia = 0
    qtdLinhas = len(matriz)
    qtdColunas = len(matriz[0])
    for i in range(qtdLinhas):
        for j in range(qtdColunas):
            if horizontal(matriz,i,j,palavra):
                ocorrencia += 1
            if vertical(matriz,i,j,palavra):
                ocorrencia += 1
            if diagonal1(matriz,i,j,palavra):
                ocorrencia += 1
            if diagonal2(matriz,i,j,palavra):
                ocorrencia += 1
    print("Palavra:", palavra)
    print("Ocorrencias:", ocorrencia)
    print("-" * 40)

# Impressão da matriz

for linha in matriz:
  print(" ".join(linha))