def cakes(recipe, available):
    cakes = []
    for ing in recipe:
        if recipe[ing] > available.get(ing, 0):
            return 0
        cakes.append(available[ing] // recipe[ing])
    return min(cakes)
        
        

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}

print(cakes(recipe, available))