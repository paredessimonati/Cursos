opposite = {'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
        } 

def dirReduc(arr):
    
    opposite = {'NORTH': 'SOUTH',
            'SOUTH': 'NORTH',
            'EAST': 'WEST',
            'WEST': 'EAST'
            } 
    
    while arr:
        for i, word in enumerate(arr):
            if len(arr) <= 1:
                return arr
            if i == len(arr) - 1:
                return arr
            if arr[i+1] == opposite[word]:
                arr.pop(i)
                arr.pop(i)
                break
    return arr





a = ['EAST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']

print(dirReduc(a))