def find_nb(m):
    n = 1
    cube_sum = 0
    while cube_sum < m:
        cube_sum += pow(n,3)
        n += 1
    return -1 if cube_sum > m else n
        
        