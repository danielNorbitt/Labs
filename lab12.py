def imprime_imagem(imagem):
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
        #retorna a parte inteira da media entre os elementos centrais
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

def filtro_negativo(imagem):
    pass

def filtro_mediana(imagem):
    novaImg = imagem[:]
    for i in range(1,len(imagem)-1):
        for j in range(1,len(imagem[0])-1):
            aux = []
            for x in range(2):
                for y in range(2):
                    aux.append(imagem[i+x][j+y])
            novaImg[i][j] = mediana(aux)
    return novaImg

def convolucao(imagem, M, D):
    # for i in range(len(imagem)):
    #     for j in range(len(imagam[0])):
    #         for x in range():
    #             for y in range():

    pass

    
# Leitura da entrada

filtro = input()
P2 = input() 

m, n = [int(x) for x in input().split()]

n255 = input() 

imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

# Aplica o filtro


imagem = filtro_mediana(imagem)


# Imprime a imagem gerada
imprime_imagem(imagem)