def matriz(lista):
    diagonal = []
    for i in range(len(lista)):
        diagonal.append(lista[i][i])  
    return(diagonal) 

def main():
    lista = []
    f = int(input(''))
    c = int(input(''))
    if f==c :
        for i in range(f):
            lista.append([])
            for j in range(c):
                n = int(input())
                lista[i].append(n)
        resultado =matriz(lista)  
        print(resultado)
    else:
        print('La matriz no es cuadrada')          

if __name__=='__main__':
    main()
