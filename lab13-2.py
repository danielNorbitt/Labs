

def ordem(matriz, prioridades):
    listDic = [{matriz[0][j]:matriz[i][j] for j in range(len(matriz[0]))} for i in range(1, len(matriz))]
    sortDic = sorted(listDic,key=lambda dic: [dic[prioridade] for prioridade in prioridades])
    data = [[ (dic[j]) for j in dic] for dic in sortDic]
    data.insert(0, matriz[0])
    return data

n = int(input())
csv = [[int(i) if i.isdigit() else i for i in input().split(",")] for _ in range(n+1)]
prioridades = input().split()

csv = ordem(csv, prioridades)
# Saída dos dados
for linha in csv:
    print('{:15s}'.format(linha[0]), ''.join(
        '{:>10}'.format(item) for item in list(linha)[1:]))
