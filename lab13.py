###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Tabela de Vendas
# Nome: 
# RA: 
###################################################

# Leitura de dados
def inputs():
    n = int(input())
    csv = []
    for _ in range(n+1):
        csv.append([int(i) if i.isdigit() else i for i in input().split(",")])
    prioridades = input().split()
    return csv,prioridades

# Ordenação dos dados
def ordemComPrioridade(matriz,prioridades):
    listT = [tuple(i) for i in matriz[1:]]
    indexPrioridade = [matriz[0].index(i) for i in prioridades]
    data = sorted(listT,key=lambda tup: [tup[x] for x in indexPrioridade])
    data.insert(0,matriz[0])
    return data

csv,prioridades = inputs()

csv = ordemComPrioridade(csv,prioridades)
# Saída dos dados
for linha in csv:
    print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in list(linha)[1:]))

