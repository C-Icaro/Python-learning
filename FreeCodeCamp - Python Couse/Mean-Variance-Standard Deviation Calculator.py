#Mean-Variance-Standard Deviation Calculator

import numpy as np

def calculate(list):

    if len(list) != 9:
        return ValueError("List must contain nine numbers.")
    
    matriz = np.array([list[0:3], list[3:6], list[6:9]]) # Cria matriz array com a lista entregue

    calculations = {} # Cria dicionário vazio

    mean = matriz.mean() # Calcula média

    axis1 = matriz[1] # Linha central
    axis2 = matriz[:,1] # Coluna Central

    calculations["mean"] = [axis1.tolist(), axis2.tolist(), float(mean)] # Add média ao dic

    variancia_colunas = matriz.var(axis=0).tolist() # Calcula a variância de todas as colunas e transforma resultado em lista
    variancia_linhas = matriz.var(axis=1).tolist() # Calcula a variância de todas as linhas e transforma resultado em lista
    variancia_total = float(matriz.var()) # Transforma array em float

    calculations["Variance"] = [variancia_colunas, variancia_linhas, variancia_total] #Add Variancia ao dicionário

    desvio_padrao_colunas = matriz.std(axis=0).tolist()
    desvio_padrao_linhas = matriz.std(axis=1).tolist()
    desvio_padrao = float(matriz.std())

    calculations["Standard Deviation"] = [desvio_padrao_colunas, desvio_padrao_linhas, desvio_padrao]

    max_colunas = matriz.max(axis = 0).tolist()
    min_colunas = matriz.min(axis = 0).tolist()
    max_linhas = matriz.max(axis = 1).tolist()
    min_linhas = matriz.min(axis = 1).tolist()

    max = float(matriz.max())
    min = float(matriz.min())

    calculations["Max"] = [max_colunas, max_linhas, max]
    calculations["Min"] = [min_colunas, min_linhas, min]

    sum_colunas = matriz.sum(axis=0).tolist()
    sum_linhas = matriz.sum(axis=1).tolist()
    sum = float(matriz.sum())

    calculations["Sum"] = [sum_colunas, sum_linhas, sum]

    return calculations

calculos = calculate([9,1,5,3,3,3,2,9,0])
print(calculos)
print("")


print("-----------------------------")
for chave, valor in calculos.items():
    print(f"{chave}: {valor}")
print("-----------------------------")
