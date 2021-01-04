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
def bubbleSort(matriz,prioridades):
    a = [matriz[0].index(i) for i in prioridades]
    litsT = [tuple(i) for i in matriz[1:]]
    data = sorted(litsT,key=lambda tup: [tup[x] for x in a])
    
    for linha in data:
        print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in list(linha)[1:]))




csv,prioridades = inputs()

bubbleSort(csv,prioridades)
# Saída dos dados
for linha in csv:
    print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))


