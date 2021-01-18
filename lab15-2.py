def indexRange(a,b,n,m):
    return a < 0 or a >=n  or b < 0 or b >= m

def chegada(a,b,c,d):
    return a == c and b == d

def saltoNulo(tabuleiro,a,b):
    return tabuleiro[a][b] == 0

def passeiPor(tabuleiro,a,b):
    return tabuleiro[a][b] !=  False

def caminhoPossivel(tabuleiro, a, b, c, d, passei):
    if chegada(a,b,c,d):
        return True
    if indexRange(a, b, len(tabuleiro), len(tabuleiro[0])) or saltoNulo(tabuleiro, a, b) or passeiPor(passei, a, b):
        return False
    passei[a][b] = True
    return caminhoPossivel(tabuleiro, a+tabuleiro[a][b], b, c, d, passei) or caminhoPossivel(tabuleiro, a-tabuleiro[a][b], b, c, d, passei) or caminhoPossivel(tabuleiro, a, b+tabuleiro[a][b], c, d, passei) or caminhoPossivel(tabuleiro, a, b-tabuleiro[a][b], c, d, passei)

def montaTabuleiro(n):
    tabuleiro = []
    for _ in range(n):
        tabuleiro.append([int(i) for i in input().split()])
    return tabuleiro

def montaPassei(n,m):
    passei = []
    for _ in range(n):
        passei.append([False] * m)
    return passei

def editaReposta(existe):
    if existe:
        return "existe caminho"
    else:
        return "nao existe caminho"

n, m = [int(i) for i in input().split()]
tabuleiro = montaTabuleiro(n)
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
passei1 = montaPassei(n,m)
passei2 = montaPassei(n,m)


ida = caminhoPossivel(tabuleiro, a, b, c, d, passei1)
volta = caminhoPossivel(tabuleiro, c, d, a, b, passei2)

print("({},{}) -> ({},{}):".format(a, b, c, d), editaReposta(ida))
print("({},{}) -> ({},{}):".format(c, d, a, b), editaReposta(volta))
