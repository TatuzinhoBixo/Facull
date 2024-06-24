def bubbleSort(dados):
    tam = len (dados)
    for v in range (0, tam, 1):
        flag = 0
        for i in range (0, tam-1, 1):
            if dados[i] > dados[i +i]:
                aux = dados [i]
                dados[i] = dados[i+1]
                dados[i+1] = aux
                #se houve uma troca, coloca a flag em 1
                flag = 1
        #encerra procecemente se não houve troca
        if flag == 0:
            return
        
            