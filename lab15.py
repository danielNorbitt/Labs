def inputs():
    n, m = [int(i) for i in input().split()]
    tabuleiro = [[int(j) for j in input().split()] for _ in range(n)]
    a, b = [int(i) for i in input().split()]
    c, d = [int(i) for i in input().split()]
    ref1 = [[0] * m for _ in range(n)]
    ref2 = [[0] * m for _ in range(n)]
    return n, m, tabuleiro, a, b, c, d, ref1,ref2

def existeCaminho(tabuleiro, a, b, c, d , n, m ,ref):
    if a == c and b == d:
        return True
    if a < 0 or a >= n or b < 0 or b >= m or tabuleiro[a][b] == 0 or ref[a][b] != 0:
        return False 
    salto = tabuleiro[a][b]
    ref[a][b] = 1
    return existeCaminho(tabuleiro,a+salto, b, c, d, n, m, ref) or existeCaminho(tabuleiro, a-salto, b, c, d, n, m, ref) or existeCaminho(tabuleiro, a, b+salto, c, d, n, m, ref) or existeCaminho(tabuleiro, a, b-salto, c, d, n, m, ref)

def printFinal(a,b,c,d,caminho1,caminho2):
    nao = "nao existe caminho"
    sim = "existe caminho"
    print("({},{}) -> ({},{}):".format(a, b, c, d), sim if caminho1 else nao)
    print("({},{}) -> ({},{}):".format(c, d, a, b), sim if caminho2 else nao)

def main():
    n, m, tabuleiro, a, b, c, d, ref1, ref2 = inputs()

    printFinal(a, b, c, d, existeCaminho(tabuleiro, a, b, c, d, n, m,
                                        ref1), existeCaminho(tabuleiro, c, d, a, b, n, m, ref2))

main()