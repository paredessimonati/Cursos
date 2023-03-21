import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

#for favorite in sorted(counts, key=lambda problem: counts[problem], reverse=True):
#    print(f"{favorite}: {counts[favorite]}")

favorite = input("Favorite: ")
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")

    #aca lo unico que hicimos fue agregar una linea para pedir input, un if para ver si el input esta en el diccionario counts e imprimir
    #el resultado