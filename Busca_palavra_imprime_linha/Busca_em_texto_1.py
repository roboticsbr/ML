
#ref_arquivo = open("av.txt","r")

#arq = open('av.txt', 'r')
#texto = arq.readlines()
for lin in open("av.txt"):
    if 'FBI' in lin:
        print(lin)

    
    
arq.close()