import  os
import  sys

os.system('CLS')

def procesarDatos(nameFile):
    archivo = open(nameFile, "r").read()
    f.close()
    return archivo

### Validaci�n de argumentos de entrada

# Validaci�n cantidad de argumentos
if len(sys.argv) != 3 :
    print("Cantidad de argumentos incorrecto")
    sys.exit(1)


# Validaci�n de archivo
if os.path.isfile(sys.argv[1])!= True:
    print("Directorio de la carta incorrecto")
    sys.exit(1)
else:
    carta = procesarDatos(sys.argv[1])

# Validaci�n de archivo
if os.path.isfile(sys.argv[2])!= True:
    print("Directorio del articulo incorrecto")
    sys.exit(1)
else:
    articulo = procesarDatos(sys.argv[2])

def esParteDict(nameFile,nameFile2):
    
    return True
    return False

# Creacion del diccionario de la carta

dict_carta = set(carta)
dict_carta = sorted(dict_carta) 

# Creacion del diccionario del articulo

dict_articulo = set(articulo)
dict_articulo = sorted(dict_articulo)

# Chequeo que se puede escribir la carta



# Validaci�n de archivo



print(pago)