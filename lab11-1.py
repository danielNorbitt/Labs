###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Beatriz Iurcic de Souza
# RA: 167292
###################################################


def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro, peca, altura_peca, largura_peca):
  for lt in range(altura_tabuleiro - altura_peca+1 ):
    for ct in range(largura_tabuleiro - largura_peca+1):
      achei = []
      for lp in range(altura_peca):
        for cp in range(largura_peca):
          if (tabuleiro[lt+lp][ct+cp] == "*" and peca[lp][cp] == ".") or (tabuleiro[lt+lp][ct+cp] == "." and peca[lp][cp] == ".") or (tabuleiro[lt+lp][ct+cp] == "." and peca[lp][cp] == "#"):
            achei.append(True)
          else:
            achei.append(False)
      if all(achei) == True:
        return (True, lt, ct)
  return (False, -1, -1)


def modifica(tabuleiro, altura_peca, largura_peca, lt, ct):
  for i in range(altura_peca):
    for j in range(largura_peca):
      if tabuleiro[lt+i][ct+j] == ".":
        tabuleiro[lt+i][ct+j] = "#"


# Leitura de dados
altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]

# Leitura do tabuleiro
tabuleiro = []
for _ in range(altura_tabuleiro):
  tabuleiro.append(list(input()))

# Leitura da peça
altura_peca, largura_peca = [int(x) for x in input().split()]

peca = []
for _ in range(altura_peca):
  peca.append(list(input()))

# Impressão da configuração atualizada do tabuleiro


status_do_jogo, lt, ct = verifica_jogo(
    tabuleiro, altura_tabuleiro, largura_tabuleiro, peca, altura_peca, largura_peca)
if status_do_jogo == True:
  modifica(tabuleiro, altura_peca, largura_peca, lt, ct)
  for linha in tabuleiro:
      print("".join(linha))
  print("O jogo deve continuar")
else:
  for linha in tabuleiro:
      print("".join(linha))
  print("Fim de jogo")
