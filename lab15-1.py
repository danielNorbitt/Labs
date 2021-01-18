def caminho(tabuleiro, a, b, c, d,aux):
    if a == c and b == d:
        return True
    if a < 0 or a >= len(tabuleiro) or b < 0 or b >= len(tabuleiro[0]) :
        return False
    if tabuleiro[a][b] == 0:
        return False
    if aux[a][b] != False:
        return False
    aux[a][b] = True
    return caminho(tabuleiro,a+tabuleiro[a][b], b, c, d,aux) or caminho(tabuleiro, a-tabuleiro[a][b], b, c, d,aux) or caminho(tabuleiro, a, b+tabuleiro[a][b], c, d,aux) or caminho(tabuleiro, a, b-tabuleiro[a][b], c, d,aux)

n, m = [int(i) for i in input().split()]
tabuleiro = []
for _ in range(n):
  tabuleiro.append([int(i) for i in input().split()])
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]
aux1 = []
aux2 = []
for _ in range(n):
  aux1.append([False] * m)
  aux2.append([False] * m)

caminho1 = caminho(tabuleiro,a,b,c,d,aux1)
caminho2 = caminho(tabuleiro,c,d,a,b,aux2)

if caminho1 :
    resposta1 = "existe caminho"
else:
    resposta1 = "nao existe caminho"

if caminho2:
    resposta2 = "existe caminho"
else:
    resposta2 = "nao existe caminho"

print("({},{}) -> ({},{}):".format(a, b, c, d),resposta1)
print("({},{}) -> ({},{}):".format(c, d, a, b),resposta2)

