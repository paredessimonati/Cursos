"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    player_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                player_count += 1

    if board == initial_state():
        return X
    if player_count % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                list.add((i, j))

    return list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    """

    if action not in actions(board):
        raise Exception("Not a valid action")

    board = deepcopy(board)
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Checking rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    # Checking columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # Else...
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        """The maximizing player picks action a in Actions(s) that produces the
        highest value of Min-Value(Result(s, a))."""

        v = -math.inf
        optimal_move = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                optimal_move = action
        return optimal_move

    else:
        """The minimizing player picks action a in Actions(s) that produces the
        lowest value of Max-Value(Result(s, a))."""

        v = math.inf
        optimal_move = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                optimal_move = action
        return optimal_move


def max_value(board):
    """
    v = -∞
    if Terminal(state):
        return Utility(state)
    for action in Actions(state):
        v = Max(v, Min-Value(Result(state, action)))
        return v
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    v = ∞
    if Terminal(state):
        return Utility(state)
    for action in Actions(state):
        v = Min(v, Max-Value(Result(state, action)))
        return v
    """

    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
