def score(dice):
    points = 0
    counts = {number: dice.count(number) for number in set(dice)}

    for number, count in counts.items():
        if count >= 3:
            points += get_score(number, 3)
            count -= 3

        if count > 0:
            single_score = get_score(number, 1)
            if single_score:
                points += single_score * count

    return points

def get_score(number, index):
    index_dict = {1: "One", 3: "Three"}
    score = {
        "Three 1": 1000,
        "Three 6":  600,
        "Three 5":  500,
        "Three 4":  400,
        "Three 3":  300,
        "Three 2":  200,
        "One 1":    100,
        "One 5":     50,
    }
    decoded = f"{index_dict[index]} {number}"
    return score.get(decoded, None)








"""version vieja"""
# def score(dice):
#     points = 0
#     while dice:
#         index = set(dice)
#         for number in index.copy():
#             count = dice.count(number)
#             if count >= 3:
#                 for _ in range(3):
#                     dice.remove(number)
#                 points += get_score(number, 3)
#                 break
#             if count >= 1:
#                 if (score := get_score(number, 1)):
#                    points += score
#                    dice.remove(number)
#                 else:
#                     for _ in range(count):
#                         dice.remove(number)
#     return points

# def get_score(number, index):
#     index_dict = {"1": "One", "3": "Three"}
#     score = {
#         "Three 1": 1000,
#         "Three 6":  600,
#         "Three 5":  500,
#         "Three 4":  400,
#         "Three 3":  300,
#         "Three 2":  200,
#         "One 1":    100,
#         "One 5":     50,
#     }
#     decoded = f"{index_dict[str(index)]} {str(number)}"
#     return None if decoded not in score else score[decoded]
    
    
    
    
    
    
print(score([2, 3, 5, 5, 5, 5, 5, 4, 2, 6, 6, 6, 6, 6]))




