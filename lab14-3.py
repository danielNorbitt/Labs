tab = []


def xero(lista):
    tab = []
    for x in lista:
        tab.append(x)
    tab.sort()


def busca(matriz, linha, coluna, palavra):
	if len(palavra) == 0:
		return True
	if linha >= len(matriz) or linha < 0 or coluna >= len(matriz[0]) or coluna < 0:
		return False
	if matriz[linha][coluna] != palavra[0]:
		xero(matriz)
		return False
	if busca(matriz, linha-1, coluna-1, palavra[1:]):
		return True
	elif busca(matriz, linha-1, coluna, palavra[1:]):
		xero(matriz)
		return True
	elif busca(matriz, linha-1, coluna+1, palavra[1:]):
		return True
	elif busca(matriz, linha, coluna-1, palavra[1:]):
		xero(matriz)
		return True
	elif busca(matriz, linha, coluna+1, palavra[1:]): 
		return True
	elif busca(matriz, linha+1, coluna-1, palavra[1:]): 
		return True
	elif busca(matriz, linha+1, coluna, palavra[1:]): 
		return True
	elif busca(matriz, linha+1, coluna+1, palavra[1:]):
		return True
	else:
		return False


# Leitura da matriz
matriz = []
x = input()
while(not x.isdigit()):
	matriz.append(x.split())
	x = input()

# Leitura das palavras

palavras = []
for i in range(int(x)):
	palavra = input()
	palavras.append(palavra)
palavras.sort()

# Processamento da busca na matriz e impressão, por palavra,
# das posições iniciais (linha e coluna)

print(40 * "-")
print("Lista de Palavras")
print(40 * "-")

for palavra in palavras:
	print("Palavra:", palavra)
	posi = []
	for x in range(len(matriz)):
		for y in range(len(matriz[0])):
			if busca(matriz, x, y, palavra):
				posi.append((x+1, y+1))
	print(("Posicoes: " + " ".join([str((linha, coluna))
								 for linha, coluna in posi])).strip())
	print(40 * "-")
