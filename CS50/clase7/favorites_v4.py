import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    #scratch, c, python = 0, 0, 0
    #se reemplaza lo de arriba por un diccionario "counts" (abrir y cerrar parentesis de llave {} significa que la variable
    #                                                       es un diccionairo)
    counts = {}
    for row in reader:
        favorite = row["language"]
        #if favorite == "Scratch":
        #    scratch += 1
        #elif favorite == "C":
        #    c += 1
        #elif favorite == "Python":
        #    python += 1
        # se borra todo esto para hacerlo mas dinamico con variables


        if favorite in counts:
            counts[favorite] += 1
        # si favorite (variable que indica lenguaje) esta en el diccionario counts agrega un 1 al contador
        else:
            counts[favorite] = 1
        # si por el contrario favorite no esta en el diccionario (un lenguaje nuevo que se agrego a la base de datos, por ejemplo)
        # al poner =1 se inicializa la variable con valor 1 para que despues cuando aparezca de nuevo el contador le agregue 1s



#def get_value(language):
#    return counts[language]
#se reemplaza lo de arriba con lamda en linea 36
    # definimos funcion get_value con un parametro language (puede ser cualquier nombre porque es solo una funcion)
    # que devuelve numero que esta en el diccionario counts definido en line#8

for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")
    # aca imprimimos la variable favorite: y para poder mostrar el numero, nos metemos al diccionario
    # counts con la llave favorite
