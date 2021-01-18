def inputs():
    n = int(input())
    csv = []
    for _ in range(n+1):
        csv.append([int(i) if i.isdigit() else i for i in input().split(",")])
    prioridades = input().split()
    return csv, prioridades



def ordemComPrioridade(matriz, prioridades):
    litDic = []
    for i in range(1,len(matriz)):
        dic = {}
        for j in range(len(matriz[0])):
            dic[matriz[0][j]] =  matriz[i][j]
        litDic.append(dic)
    data = sorted(litDic, key=lambda tup: [tup[x] for x in prioridades])
    m = []
    for dic in data:
        aux = []
        for j in dic:
            aux.append(dic[j])
        m.append(aux)
    m.insert(0,matriz[0])
    return m


csv, prioridades = inputs()

csv = ordemComPrioridade(csv, prioridades)

for linha in csv:
    print('{:15s}'.format(linha[0]), ''.join(
        '{:>10}'.format(item) for item in list(linha)[1:]))
