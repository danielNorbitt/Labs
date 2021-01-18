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



def busca_palavra(matriz, linha, coluna, palavra):
	if len(palavra) == 0:
		return True
	if linha >= len(matriz) or linha < 0 or  coluna >= len(matriz[0]) or coluna < 0:
		return False
	if matriz[linha][coluna] != palavra[0]:
		return False
	return busca_palavra(matriz, linha-1, coluna-1, palavra[1:]) or \
			busca_palavra(matriz, linha-1, coluna, palavra[1:]) or \
			busca_palavra(matriz, linha-1, coluna+1, palavra[1:]) or \
			busca_palavra(matriz, linha, coluna-1, palavra[1:]) or \
			busca_palavra(matriz, linha, coluna+1, palavra[1:]) or \
			busca_palavra(matriz, linha+1, coluna-1, palavra[1:]) or \
			busca_palavra(matriz, linha+1, coluna, palavra[1:]) or \
			busca_palavra(matriz, linha+1, coluna+1, palavra[1:])




# Leitura da matriz

matriz = []
x=input()
while(not x.isdigit()):
	matriz.append(x.split())
	x=input()

# Leitura das palavras

palavras = []
for i in range(int(x)):
	p=input()
	palavras.append(p)




# Processamento da busca na matriz e impressão, por palavra,
# das posições iniciais (linha e coluna)

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")

for palavra in sorted(palavras):
	print("Palavra:", palavra)
	posicoes=[]
	for x in range(len(matriz)):
		for y in range(len(matriz[0])):
			if busca_palavra(matriz,x,y,palavra):
				posicoes.append((x+1,y+1))
	print(("Posicoes: " + " ".join([str((linha, coluna)) for linha, coluna in posicoes])).strip())
	print(40 * "-")
