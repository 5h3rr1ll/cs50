"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

moves = set()

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
        x += row.count("X")
        o += row.count("O")
    
    if x == 0 and o == 0:
        return "X"
    elif x > o:
        return "O"
    return "X"
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
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
    
    if action in moves:
        new_board[action[0]][action[1]] = player(board)
        return new_board

    raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    """Check if in one row are only one symbol like X or O = win state"""
    for row in board:
        if row.count(row[0]) == 3 and row[0] != EMPTY:
            return(row[0])

    """Check if in each row at the same poition is the same symbol like X or O = win state"""
    for i,row in enumerate(board):
        print("BORAD: ", board)
        if board[i][0] != EMPTY and board[i][0] == board[i+1][0] == board[i+2][0]:
            return(board[i][0])

    for i,row in enumerate(board):
        if board[i][1] != EMPTY and board[i][1] == board[i+1][1] == board[i+2][1]:
            return(board[i][1])

    for i,row in enumerate(board):
        if board[i][2] != EMPTY and board[i][2] == board[i+1][2] == board[i+2][2]:
            return(board[i][2])

    """Check if in the middle (1) row at the poition 1 and in row 0 and 1 and position 0 and 2 is the same symbol like X or O = win state"""


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
