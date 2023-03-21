from time import process_time


puzzle = [[0,0,0,0,7,0,0,0,0],
          [6,0,0,0,0,5,0,0,0],
          [0,0,0,0,0,0,0,6,0],
          [8,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1],
          [7,0,0,0,2,0,0,0,0],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,0,1,0,0,0,0],
          [0,0,0,0,8,0,0,0,0]]


def sudoku():
    """return the solved puzzle as a 2d array of 9 x 9"""
    start_time = process_time()
    solve(puzzle)
    end_time = process_time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    return puzzle


def solve(puzzle):
    
    row, col = find_empty(puzzle)
    if row is None and col is None:
        return True
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve(puzzle):
                return True
            puzzle[row][col] = 0
    return False


def find_empty(puzzle):
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j
    return None, None

def is_valid(puzzle, row, col, num):
    

    if num in puzzle[row]:
        return False
    if num in [puzzle[i][col] for i in range(9)]:
        return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[row_start + i][col_start + j] == num:
                return False
    return True

if __name__ == "__main__":
    sudoku()
    
