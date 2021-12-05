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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """ 
    x = 0
    o = 0
    
    for row in board:
        x += row.count(X)
        o += row.count(O)
    
    if x == 0 and o == 0:
        return X
    elif x > o:
        return O
    return X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()

    for idx, row in enumerate(board):
        for idy, move in enumerate(row):
            if move == EMPTY:
                moves.add((idx, idy))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    new_board = deepcopy(board)

    if action in actions(board):
        new_board[action[0]][action[1]] = player(board)
        return new_board

    raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one, otherweise None.
    """
    
    """Check if in one row are only one symbol like X or O = win state"""
    for row in board:
        if row.count(row[0]) == 3 and row[0] != EMPTY:
            return(row[0])

    """Check if in each row at the same poition is the same symbol like X or O = win state"""
    for i,row in enumerate(board):
        if board[0][i] != EMPTY and board[0][i] == board[1][i] == board[2][i]:
            return(board[0][i])

    """Check if diagonals are the same symbol like X or O = win state"""
   
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return(board[0][0])

    elif board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return(board[0][2])
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 if no winner.
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
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
        if terminal(board):
            # If there is winner or no possivle moves left, return value of this end state and None.
            # None indicates the end of the tree.
            return utility(board), None

        # -inf is the lowest possible value for a state
        value = float('-inf')
        move = None
        # For each action, find the value of the next state and compare it to the current value.
        for action in actions(board):
            next_value, act = min_value(result(board, action))
            if next_value == 1:
                return next_value, action
            elif next_value > value:
                value = next_value
                move = action
        return value, move

def min_value(board):
        if terminal(board):
            return utility(board), None

        value = float('inf')
        move = None
        for action in actions(board):
            next_value, act = max_value(result(board, action))
            if value == -1:
                    return value, move
            elif next_value < value:
                value = next_value
                move = action
        return value, move
