import math
import random

def evaluate(board):
    # Evaluation function for Tic-Tac-Toe
    for row in board:
        if all(cell == 1 for cell in row):
            return 1
        elif all(cell == -1 for cell in row):
            return -1

    for col in zip(*board):
        if all(cell == 1 for cell in col):
            return 1
        elif all(cell == -1 for cell in col):
            return -1

    if all(board[i][i] == 1 for i in range(3)) or all(board[i][2 - i] == 1 for i in range(3)):
        return 1
    elif all(board[i][i] == -1 for i in range(3)) or all(board[i][2 - i] == -1 for i in range(3)):
        return -1

    return 0

def is_terminal(board):
    # Check if the current state of the board is a terminal state (game over)
    return evaluate(board) != 0 or len(empty_cells(board)) == 0

def empty_cells(board):
    # Return a list of empty cells on the board
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

def minimax(board, depth, maximizing_player):
    if is_terminal(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for cell in empty_cells(board):
            board[cell[0]][cell[1]] = 1
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = 0
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for cell in empty_cells(board):
            board[cell[0]][cell[1]] = -1
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = 0
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for cell in empty_cells(board):
        board[cell[0]][cell[1]] = 1
        move_val = minimax(board, 0, False)
        board[cell[0]][cell[1]] = 0

        if move_val > best_val:
            best_move = cell
            best_val = move_val

    return best_move

# Example usage for Tic-Tac-Toe:
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Player is 1, opponent is -1
while not is_terminal(board):
    # Player's move
    player_move = find_best_move(board)
    board[player_move[0]][player_move[1]] = 1

    if is_terminal(board):
        break

    # Opponent's move
    opponent_move = find_best_move(board)
    board[opponent_move[0]][opponent_move[1]] = -1

print("Final Board:")
for row in board:
    print(row)
