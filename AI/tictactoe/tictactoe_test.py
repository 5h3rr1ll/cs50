from tictactoe import initial_state, player, result, actions, winner 

EMPTY = None
board = initial_state()

def test_initial_board():
    assert board == [[EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY]]

def test_player_x():
    assert player(board) == "X"

def test_player_y():
    board = [["X", EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY],
              [EMPTY, EMPTY, EMPTY]]
    assert player(board) == "O"

def test_tictactoe_actions():
    assert actions(board) == {(0, 1), (1, 2), (0, 0), (2, 1), (2, 0), (1, 1), (2, 2), (1, 0), (0, 2)}

def test_tictactoe_result():
    assert result(board, (0, 0)) == [["X", EMPTY, EMPTY],
                                     [EMPTY, EMPTY, EMPTY],
                                     [EMPTY, EMPTY, EMPTY]]

def test_winner_x_h_row():
    assert winner([["X", "X", "X"],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == "X"

def test_winner_o_h_row():
    assert winner([["O", "O", "O"],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == "O"

def test_no_winner_h_row():
    assert winner([["X", "O", "X"],
                   [EMPTY, EMPTY, EMPTY],
                   [EMPTY, EMPTY, EMPTY]]) == None

def test_winner_x_v_row1():
    assert winner([["X", EMPTY, EMPTY],
                   ["X", EMPTY, EMPTY],
                   ["X", EMPTY, EMPTY]]) == "X"

def test_winner_x_v_row2():
    assert winner([[EMPTY, "X", EMPTY],
                   [EMPTY, "X", EMPTY],
                   [EMPTY, "X", EMPTY]]) == "X"

def test_winner_x_v_row3():
    assert winner([[EMPTY, EMPTY, "X"],
                   [EMPTY, EMPTY, "X"],
                   [EMPTY, EMPTY, "X"]]) == "X"