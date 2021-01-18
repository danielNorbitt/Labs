###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caça-Palavras 3.0
# Nome:
# RA:
###################################################

"""
Esta função recebe como parâmetro uma matriz, uma posição inicial na
matriz determinada pelos parâmetros linha e coluna e uma palavra que
	deve ser buscada em todas as direções (norte, sul, leste, oeste,
	nordeste, sudeste, noroeste e sudoeste) a partir da posição inicial.

Caso a palavra seja encontrada a partir da posição inicial a função
deve retornar o valor True. Caso contrário, a função de retornar o
valor False.
"""

def intervaloValido(linha,coluna,n,m):
    return linha >= n or linha < 0 or coluna >= m or coluna < 0
def acabou(palavra):
    return len(palavra) == 0 
def letraCerta(linha,coluna,palavra,matriz):
    return matriz[linha][coluna] != palavra[0]
def subPalavra(palavra):
    return palavra[1:]
def busca_palavra(matriz, linha, coluna, palavra):
	if acabou(palavra):
		return True
	if intervaloValido(linha, coluna, len(matriz), len(matriz[0])) or letraCerta(linha, coluna, palavra, matriz):
		return False
	novaPalavra = subPalavra(palavra)
	return  busca_palavra(matriz, linha-1, coluna-1, novaPalavra) or \
            busca_palavra(matriz, linha+1, coluna+1, novaPalavra) or \
			busca_palavra(matriz, linha-1, coluna, novaPalavra) or \
			busca_palavra(matriz, linha+1, coluna, novaPalavra) or \
			busca_palavra(matriz, linha, coluna-1, novaPalavra) or \
			busca_palavra(matriz, linha+1, coluna-1, novaPalavra) or \
			busca_palavra(matriz, linha, coluna+1, novaPalavra) or \
			busca_palavra(matriz, linha-1, coluna+1, novaPalavra) 

def inputMatriz():
	matriz = []
	x = input()
	while (True):
		if x.isdigit():
			return int(x), matriz
		matriz.append(x.split())
		x = input()
def inputPalavra(x):
	palavras = []
	for _ in range(x):
		palavras.append(input())
		palavras.sort()
	return palavras
def printFinal(palavras,matriz):
	print(40 * "-")
	print("Lista de Palavras")
	print(40 * "-")
	for palavra in palavras:
		print("Palavra:", palavra)
		posicoes = []
		for i in range(len(matriz)):
			for j in range(len(matriz[0])):
				if busca_palavra(matriz, i, j, palavra):
					posicoes.append((i+1, j+1))
		print(("Posicoes: " + " ".join([str((linha, coluna))
									for linha, coluna in posicoes])).strip())
		print(40 * "-")


x, matriz = inputMatriz()
palavras = inputPalavra(x)

printFinal(palavras,matriz)





