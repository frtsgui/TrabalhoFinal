from time import time
import numpy as np

def agirEmVolta(matriz, m, n, condicao, acao):
    if m==0:
        if n==0: 
            for i in range(0,2):
                for j in range(0,2):
                    if eval(condicao): exec(acao)
        elif n==len(matriz[0])-1:
            for i in range(0,2):
                for j in range(-1,1):
                    if eval(condicao): exec(acao)
        else: 
            for i in range(0,2):
                for j in range(-1,2):
                    if eval(condicao): exec(acao)
    elif m==len(matriz)-1:
        if n==0:
            for i in range(-1,1):
                for j in range(0,2):
                    if eval(condicao): exec(acao)
        elif n==len(matriz[0])-1:
            for i in range(-1,1):
                for j in range(-1,1):
                    if eval(condicao): exec(acao)
        else:
            for i in range(-1,1):
                for j in range(-1,2):
                    if eval(condicao): exec(acao)
    else:
        if n==0:
            for i in range(-1,2):
                for j in range(0,2):
                    if eval(condicao): exec(acao)
        elif n==len(matriz[0])-1:
            for i in range(-1,2):
                for j in range(-1,1):
                    if eval(condicao): exec(acao)
        else:
            for i in range(-1,2):
                for j in range(-1,2):
                    if eval(condicao): exec(acao)
    

def segmentacao(tela):
    global pertence
    pertence = [[[] for j in range(len(tela[0]))] for i in range(len(tela))]
    # for m in range(len(tela)):
    #     for n in range(len(tela[0])):
    #         agirEmVolta(tela, m, n, "matriz[m,n] == '-' and matriz[m+i,n+j] in ['1', '2', '3', '4', '5', '6', '7', '8']", "pertence[m][n].append([m+i,n+j])")

    # pertenceUnico = [[]]
    # for m in range(len(tela)):
    #     for n in range(len(tela[0])):
    #         if sorted(pertence[m][n]) not in pertenceUnico and pertence[m][n] != []:
    #             pertenceUnico.append(sorted(pertence[m][n]))
    
    # regiao = [[] for i in range(len(pertenceUnico))]
    # for m in range(len(pertence)):
    #     for n in range(len(pertence[m])):
    #         regiao[pertenceUnico.index(pertence[m][n])].append([m,n])

    for m in range(len(tela)):
        for n in range(len(tela[0])):
            agirEmVolta(tela, m, n, "matriz[m,n] in ['1', '2', '3', '4', '5', '6', '7', '8'] and matriz[m+i,n+j] == '-'", "pertence[m+i][n+j].append([m,n])")
    
    pertenceUnico = [[]]
    for m in range(len(tela)):
        for n in range(len(tela[0])):
            if sorted(pertence[m][n]) not in pertenceUnico and pertence[m][n] != []:
                pertenceUnico.append(sorted(pertence[m][n]))
    
    infoRegiao = [[] for i in range(len(pertenceUnico))]
    for m in range(len(pertence)):
        for n in range(len(pertence[m])):
            if tela[m,n] == '-':
                infoRegiao[pertenceUnico.index(pertence[m][n])].append([m,n])

    regioes = -1*np.ones(np.shape(tela), int)
    for m in range(len(infoRegiao)):
        for n in infoRegiao[m]:
            regioes[tuple(n)] = m

    print(regioes)
                    

    return infoRegiao