with open("av.txt", "r") as arq:
    for linha in arq:
        if linha.find('computador') > -1:
            print (linha)