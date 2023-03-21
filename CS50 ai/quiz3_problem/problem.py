import scipy.optimize
"""
The following two questions will both ask you about the optimization problem
described below.
A farmer is trying to plant two crops, Crop 1 and Crop 2, and wants to maximize
his profits. The farmer will make $500 in profit from each acre of Crop 1
planted, and will make $400 in profit from each acre of Crop 2 planted. 

However, the farmer needs to do all of his planting today, during the 12
hours between 7am and 7pm. Planting an acre of Crop 1 takes 3 hours, and
planting an acre of Crop 2 takes 2 hours.

The farmer is also limited in terms of supplies: he has enough supplies
to plant 10 acres of Crop 1 and enough supplies to plant 4 acres of Crop 2.

Assume the variable C1 represents the number of acres of Crop 1 to plant,
and the variable C2 represents the number of acres of Crop 2 to plant.
"""



# Objective Function: 500C1 + 400C2
# Constraint 1: 3C1 + 2C2 ≤ 12
# Constraint 2: 1C1 + 0C2<= 10 
# Constraint 3: 1C2 + 0C1<= 4


result = scipy.optimize.linprog(
    [500, 400],  # Cost function: 500C1 + 400C2
    A_ub=[[3, 2], [1, 0], [0, 1]],  # Coefficients for inequalities
    b_ub=[12, 10, 4]  # Constraints for inequalities: 20 and -90
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} acres")
    print(f"X2: {round(result.x[1], 2)} acres")
else:
    print("No solution")