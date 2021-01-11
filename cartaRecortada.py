import  os
import  sys

os.system('CLS')

def procesarDatos(nameFile):
    f = open(nameFile, "r")
    archivo = f.read()
    f.close()
    return archivo

### Validación de argumentos de entrada

# Validación cantidad de argumentos
if len(sys.argv) != 3 :
    print("Cantidad de argumentos incorrecto")
    sys.exit(1)


# Validación de archivo
if os.path.isfile(sys.argv[1])!= True:
    print("Directorio de la carta incorrecto")
    sys.exit(1)
else:
    carta = procesarDatos(sys.argv[1])

# Validación de archivo
if os.path.isfile(sys.argv[2])!= True:
    print("Directorio del articulo incorrecto")
    sys.exit(1)
else:
    articulo = procesarDatos(sys.argv[2])

def chequearSubDict( subDict, testDict ):
    i = 0
    j = 0
    while(i < len(testDict) and  j < len(subDict)):
        if(subDict[j] == testDict[i]):
            i = i + 1
            j = j + 1
        elif(subDict[j] > testDict[i]):
            i = i + 1
        else:
            return False
    
    if (j == len(subDict)):
        return True
    else:
        return False
    


# Creacion del diccionario de la carta

# Utilizo set() para quedarme con los elementos unicos de la lista, tener en cuenta que dictCarta es de tipo Set 
dictCarta = set(carta) 

# Utilizo sorted() para ordenar los elementos, dictCarta es de tipo Lista 
dictCarta = sorted(dictCarta) 

# Creacion del diccionario del articulo

# Utilizo set() para quedarme con los elementos unicos de la lista, tener en cuenta que dictArticulo es de tipo Set
dictArticulo = set(articulo) 

# Utilizo sorted() para ordenar los elementos, dictArticulo es de tipo Lista 
dictArticulo = sorted(dictArticulo) 

# Chequeo que se puede escribir la carta
if (chequearSubDict(dictCarta, dictArticulo)):
    print("Se puede imprimir la carta con las letras del articulo")
else:
    print("No se puede imprimir la carta con las letras del articulo")
    sys.exit(1)

# Escribo la carta a partir del diccionario de letras recortadas

# Inicializo una lista para almacenar la carta a escribir con las letras recortadas
cartaRecortada = [None] * len(carta)

for i in range(0,len(carta)):
    # Busco dentro del diccionario del articulo la letra de la carta que corresponde
    # para la carta de letras recortadas para ser asignada. Puede que exista una 
    # solucion mas elegante.
    cartaRecortada[i] = dictArticulo[dictArticulo.index(carta[i])]

# Imprimo como tipo string a mi carta hecha con letras recortadas
print("".join(cartaRecortada))

