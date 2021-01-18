aux = []

def copia(lista):
    aux = []
    for x in lista:
        aux.append(x)
    aux.sort()


def caminho(tabuleiro, a, b, c, d, matrizReferencia):
    if a == c and b == d:
        return True
    if a < 0 or a >= len(tabuleiro) or b < 0 or b >= len(tabuleiro[0]) or tabuleiro[a][b] == 0 or matrizReferencia[a][b] != 0:
        return False
    copia(tabuleiro)
    matrizReferencia[a][b] = 1
    return caminho(tabuleiro, a+tabuleiro[a][b], b, c, d,  matrizReferencia) or caminho(tabuleiro, a-tabuleiro[a][b], b, c, d,  matrizReferencia) or caminho(tabuleiro, a, b+tabuleiro[a][b], c, d,  matrizReferencia) or caminho(tabuleiro, a, b-tabuleiro[a][b], c, d,  matrizReferencia)


def printCaminhos(a, b, c, d, caminho1, caminho2):
    nao = "nao existe caminho"
    sim = "existe caminho"
    resposta1 = sim if caminho1 else nao
    resposta2 = sim if caminho2 else nao
    print("({},{}) -> ({},{}):".format(a, b, c, d), resposta1)
    print("({},{}) -> ({},{}):".format(c, d, a, b), resposta2)

n, m = [int(i) for i in input().split()]
tabuleiro = [[int(j) for j in input().split()] for x in range(n)]
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
matrizReferencia1 = [[0] * m for x in range(n)]
matrizReferencia2 = [[0] * m for x in range(n)]

printCaminhos(a, b, c, d, caminho(tabuleiro, a, b, c, d, 
                                         matrizReferencia1), caminho(tabuleiro, c, d, a, b,  matrizReferencia2))


