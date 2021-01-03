import copy

def inputs():
    filtro = input()
    _ = input()
    m,n = [int(i) for i in input().split()]
    _ = int(input())
    imagem = []
    for _ in range(n):
        imagem.append([int(x) for x in input().split()])
    return filtro,n,m,imagem

def printImage(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))

def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

def retiraBorda(imagem):
    novaImg = copy.deepcopy(imagem)
    for i in range(len(imagem)):
        del(novaImg[i][0])
        _ = novaImg[i].pop()
    novaImg.pop()
    del(novaImg[0])
    return novaImg

def convolucao(imagem,filtro,D):
    novaImg = copy.deepcopy(imagem)
    for i in range(1,len(imagem)-1):
        for j in range(1,len(imagem[0])-1):
            soma = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    soma += filtro[x+1][y+1]*imagem[i+x][j+y]
            novaImg[i][j] = max(min(255,soma//D),0)
    return retiraBorda(novaImg)       

def filtroMediana(imagem):
    novaImg = copy.deepcopy(imagem)
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            aux = []
            n = -1
            h = 2
            g = -1
            k = 2
            if i == 0:
                n = 0
            if j == 0:
                g = 0
            if i == len(imagem)-1:
                h = 1
            if j == len(imagem[0])-1:
                k = 1
            for x in range(n,h):
                for y in range(g,k):
                    aux.append(imagem[i+x][j+y])
            novaImg[i][j] = mediana(aux)
    return novaImg

def filtroNegativo(imagem):
    novaImg = copy.deepcopy(imagem)
    for i in range(len(imagem)):
        for j in range(len(imagem[0])):
            novaImg[i][j] = 255 - novaImg[i][j] 
    return novaImg

def filtroBlur(imagem):
    filtroB = [[1,1,1] for _ in range(3)]
    D = 9
    return convolucao(imagem,filtroB,9)

def filtroEdge(imagem):
    filtroE = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    D = 1
    return convolucao(imagem,filtroE,D)

def filtroSharpen(imagem):
    filtroS = [[0,-1,0],[-1,5,-1],[0,-1,0]] 
    D = 1
    return convolucao(imagem,filtroS,D)

def aplicaFiltro(filtro,imagem):
    if filtro == "mediana":
        novaImagem = filtroMediana(imagem)
    elif filtro == "negativo":
        novaImagem = filtroNegativo(imagem)
    elif filtro == "blur":
        novaImagem = filtroBlur(imagem)
    elif filtro == "edge-detect":
        novaImagem = filtroEdge(imagem)
    else:
        novaImagem = filtroSharpen(imagem)
    return novaImagem

filtro,n,m,imagem = inputs()

novaImagem = aplicaFiltro(filtro,imagem)

printImage(novaImagem)