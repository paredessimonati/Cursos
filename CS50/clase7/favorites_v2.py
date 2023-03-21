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


#print(f"Scratch: {scratch}")
#print(f"C: {c}")
#print(f"Python: {python}")


for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")
    # aca imprimimos la variable favorite: y para poder mostrar el numero, nos metemos al diccionario
    # counts con la llave favorite (sorted no es necesario, es solo una funcion que ordena alfabeticamente
    # tambien puede agregarsele reverse=True para que sea al reves)