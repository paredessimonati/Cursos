

def dirReduc(arr):
    while True:
        for i, word in enumerate(arr):
            if i + 1 == opposite[word]:
                arr.pop(i)
                arr.pop(i+1)
            


opposite = {'NORTH': 'SOUTH',
            'SOUTH': 'NORTH',
            'EAST': 'WEST',
            'WEST': 'EAST'
            } 



a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(a))