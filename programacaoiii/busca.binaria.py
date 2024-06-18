def buscaBinaria (inicio, fim, dados, buscado):
    while (inicio <= fim):
        meio = int ((inicio + fim) /2)
        if (buscado > dados [meio]):
            inicio = meio + 1
        elif (buscado < dados [meio]):
            fim = meio - 1
        else:
            return meio
    return -1