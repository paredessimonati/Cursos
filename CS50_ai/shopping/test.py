import csv

def convert(cell):
    month_dict = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "June": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }
    if cell in month_dict:
        return month_dict[cell]
    elif cell == "Returning_Visitor" or cell is True:
        return 1
    else:
        return 0 
    

with open("shopping.csv") as data:
    reader = csv.reader(data)
    header = next(data)
    evidence = []
    labels = []
    list_of_ints = [0,2,4,11,12,13,14,15,16]
    convert_cells = [10, 15, 16]
    
    for row in reader:
        for i, cell in enumerate(row):
            if i in convert_cells:
                evidence.append(convert(cell))
            elif i in list_of_ints:
                evidence.append(int(cell))
            elif i == 17:
                labels.append(cell)
            else:
                evidence.append(float(cell))
            
print(evidence[0])