###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: 
# RA: 
###################################################


def ref(peca,altura_peca,largura_peca):
    ref = []
    first = peca[0].index("#")
    for x in range(altura_peca):
        for y in range(largura_peca):
            if peca[x][y] == "#":
                ref.append((x,y-first))
    ref.pop(0)
    return ref



"""
Esta função recebe seis parâmetros:
- tabuleiro: a configuração inicial do tabuleiro;
- altura_tabuleiro: o valor da altura do tabuleiro;
- largura_tabuleiro: o valor da largura do tabuleiro;
- peca: a configuração da peça a ser inserida;
- altura_peca: o valor da altura da peça a ser inserida;
- largura_peca: o valor da largura da peça a ser inserida.

A função deve retornar a configuração atualizada do tabuleiro 
e o status do jogo ("O jogo deve continuar" ou "Fim de jogo")
"""
def verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,peca, altura_peca, largura_peca):
    status_do_jogo = "Fim de jogo"
    pecaRef = ref(peca,altura_peca,largura_peca)
    if altura_peca < altura_tabuleiro or largura_peca < largura_tabuleiro:
        espacoLivre = False
        for i in range(altura_tabuleiro):
            for j in range(largura_tabuleiro):
                if tabuleiro[i][j] == "." and not espacoLivre:
                    for index in range(len(pecaRef)):
                        x,y = pecaRef[index]
                        if tabuleiro[i+x][j+y] != ".":
                            espacoLivre = False
                            break
                        espacoLivre = True
                        livre = (i,j)
        if espacoLivre:
            i,j = livre
            tabuleiro[i][j] = "#"
            for index in range(len(pecaRef)):
                x,y = pecaRef[index]
                tabuleiro[i+x][j+y] = "#"
            status_do_jogo = "O jogo deve continuar"
    return tabuleiro, status_do_jogo

def inputString(altura):
    matriz = []
    for _ in range(altura):
        matriz.append(list(input()))
    return matriz

# Leitura de dados

altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]

# Leitura do tabuleiro

# Dica: use a função list() para transformar uma srting numa lista de caracteres
tabuleiro = inputString(altura_tabuleiro)

altura_peca, largura_peca = [int(x) for x in input().split()]

peca = inputString(altura_peca)

# Leitura da peça

# Dica: use a função list() para transformar uma srting numa lista de caracteres

# Impressão da configuração atualizada do tabuleiro

tabuleiro, status_do_jogo = verifica_jogo(tabuleiro, altura_tabuleiro, largura_tabuleiro,peca, altura_peca, largura_peca)



for linha in tabuleiro:
    print("".join(linha))

# Impressão do status do jogo

print(status_do_jogo)