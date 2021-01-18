###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome: 
# RA: 
###################################################
m = []

def entrada():
    matriz = []
    x=input()
    while(not x.isdigit()):
        matriz.append(x.split())
        x=input()

    palavras = []
    for _ in range(int(x)):
        palavra=input()
        palavras.append(palavra)

    return matriz,sorted(palavras)

def matrix(matriz):
    m = []
    for i in range(len(matriz)):
        aux = []
        for j in range(len(matriz[0])):
            aux.append(matriz[i][j])
        m.append(aux)

def buscaP(matriz, linha, coluna, palavra,i):
    if len(palavra) == i:
        return True
    if linha >= len(matriz) or linha < 0 or  coluna >= len(matriz[0]) or coluna < 0:
        return False
    if matriz[linha][coluna] != palavra[i]:
        return False
    matrix(matriz)
    return buscaP(matriz, linha-1, coluna-1, palavra,i+1) or buscaP(matriz, linha+1, coluna-1, palavra,i+1) or buscaP(matriz, linha, coluna+1, palavra,i+1) or buscaP(matriz, linha-1, coluna+1, palavra,i+1) or buscaP(matriz, linha+1, coluna, palavra,i+1) or buscaP(matriz, linha, coluna-1, palavra,i+1) or buscaP(matriz, linha-1, coluna, palavra,i+1) or buscaP(matriz, linha+1, coluna+1, palavra,i+1)


matriz,palavras = entrada()


print(40 * "-")
print("Lista de Palavras")
print(40 * "-")

for palavra in palavras:
	print("Palavra:", palavra)
	posicoes=[ ]
	for x in range(len(matriz)):
		for y in range(len(matriz[0])):
			if buscaP(matriz,x,y,palavra,0):
				posicoes.append((x+1,y+1))
	print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
	print(40 * "-")
