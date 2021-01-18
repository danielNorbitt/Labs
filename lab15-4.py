tab = []

def xero(lista):
    tab = []
    for x in lista:
        tab.append(x)
    tab.sort()


def trilha(tabuleiro, a, b, c, d, matrix):
    if a == c and b == d:
        return True
    if a < 0 or a >= len(tabuleiro) or b < 0 or b >= len(tabuleiro[0]) or tabuleiro[a][b] == 0 or matrix[a][b] != False:
        return False
    matrix[a][b] = True
    if trilha(tabuleiro, a+tabuleiro[a][b], b, c, d,  matrix):
        xero(tabuleiro) 
        return  True
    elif trilha(tabuleiro, a-tabuleiro[a][b], b, c, d,  matrix):
        return True
    elif trilha(tabuleiro, a, b+tabuleiro[a][b], c, d,  matrix):
        return True
    elif trilha(tabuleiro, a, b-tabuleiro[a][b], c, d,  matrix):
        return True
    else:
        xero(tabuleiro)
        return False


n, m = [int(i) for i in input().split()]
tabuleiro = [[int(j) for j in input().split()] for x in range(n)]
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
matrix1 = [[False] * m for x in range(n)]
matrix2 = [[False] * m for x in range(n)]


n = "nao existe caminho"
s = "existe caminho"
r1 = s if trilha(tabuleiro, a, b, c, d,matrix1) else n
r2 = s if trilha(tabuleiro, c, d, a, b,  matrix2) else n
print("({},{}) -> ({},{}):".format(a, b, c, d), r1)
print("({},{}) -> ({},{}):".format(c, d, a, b), r2)
