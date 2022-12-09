# 0-8: Número de Minas em volta (não revelado)
# 9: Tem mina (não revelado)
# 10-18: Número de Minas em volta (revelado)
# 19: Tem mina (revelado)
# 20-28: Número de Minas em volta (flag)
# 29: Tem mina (flag)

import numpy as np
from scipy import signal
from utils import *

def distMinas(numLin = 3, numCol = 4, numMinas = 5):
    campo = np.zeros([numLin, numCol], int)
    if numMinas >= numLin*numCol: print('Número de minas inválido')
    else:
        for n in range(numMinas):
            posMina = tuple(np.random.randint(0,[numLin, numCol]))
            while campo[posMina] != 0:
                posMina = tuple(np.random.randint(0,[numLin, numCol]))
            campo[posMina] = 9
    return campo

def contMinas(campo):
    somaMinas = np.ones([3,3], int)
    somaMinas[1,1] = 10
    campo = signal.fftconvolve(campo, somaMinas, 'same')
    campo = np.array([[min(round(x/9),9) for x in linha] for linha in campo])
    return campo

def revelaEmVolta(campo, m, n):
    if campo[m,n]==10:
        agirEmVolta(campo, m, n, 'matriz[m+i,n+j] <= 9', 'matriz[m+i,n+j] += 10')
    return campo

def marcar(campo, m, n):
    if campo[m,n] <= 9: campo[m][n] += 20
    elif campo[m,n] >= 20: campo[m][n] -= 20
    return campo

def escolher(campo, m, n):
    if campo[m,n] <= 9: campo[m][n] += 10
    campo = revelaEmVolta(campo, m, n)
    reveladoEmVolta = np.array([[False for linha in coluna] for coluna in campo])
    reveladoEmVolta[m,n] = True
    
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            if (campo[i,j] == 10) and (not reveladoEmVolta[i,j]):
                campo = revelaEmVolta(campo, i, j)
                reveladoEmVolta[i,j] = True

    for i in range(len(campo)):
        for j in range(len(campo[0])):
            if (campo[len(campo)-1-i,len(campo[0])-1-j] == 10) and (not reveladoEmVolta[len(campo)-1-i,len(campo)-1-j]):
                campo = revelaEmVolta(campo, len(campo)-1-i, len(campo)-1-j)
                reveladoEmVolta[len(campo)-1-i,len(campo)-1-j] = True
    return campo

def exibir(campo):
    tela = np.array([['-' for x in linha] for linha in campo])
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            if campo[i,j] in range(10,19): tela[i,j] = campo[i,j] % 10
            if campo[i,j] == 19: tela[i,j] = 'X'
            if campo[i,j] in range(20,30): tela[i,j] = 'O'
    return tela

def fimJogo(campo, numMinas):
    numMinasEscondidas = 0
    numMinasMarcadas = 0
    numCasasNaoReveladas = 0

    for i in range(len(campo)):
        for j in range(len(campo[0])):
            if campo[i,j] == 9: numMinasEscondidas += 1
            if campo[i,j] == 19: return -1
            if campo[i,j] == 29: numMinasMarcadas += 1
            if campo[i,j] < 10: numCasasNaoReveladas +=1
                
    if (numMinasMarcadas == numMinas) or (numCasasNaoReveladas + numMinasMarcadas == numMinas): return 1
    else: return 0

if __name__ == "__main__":
    numLin = 10
    numCol = 10
    numMinas = 5
    campo = distMinas(numLin,numCol,numMinas)
    campo = contMinas(campo)
    global tela
    while(fimJogo(campo,numMinas) == 0):
        start = time()
        tela = exibir(campo)
        print(tela)
        regiao = segmentacao(tela)
        end = time()
        print(end - start)
        # for r in regiao[1:]: print(r)
        action = input("[r]evelar, [m]arcar ou [s]air? ")
        if action == 'r':
            x = int(input("Insira a linha: "))
            y = int(input("Insira a coluna: "))
            campo = escolher(campo, x, y)
        elif action == 'm':
            x = int(input("Insira a linha: "))
            y = int(input("Insira a coluna: "))
            campo = marcar(campo, x, y)
        elif action == 's': break
        print(fimJogo(campo,numMinas))

    fim = campo % 10 + 10
    print(exibir(fim))