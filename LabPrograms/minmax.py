import math

# Constants for player symbols
X = 'X'
O = 'O'
EMPTY = ' '


def evaluate(board):
    """
    Evaluate the current board state.
    Returns +1 if X wins, -1 if O wins, 0 if it's a tie or the game is ongoing.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return 1
        elif row.count(O) == 3:
            return -1

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == X:
                return 1
            elif board[0][col] == O:
                return -1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == X:
            return 1
        elif board[1][1] == O:
            return -1

    # Check for tie
    if any(EMPTY in row for row in board):
        return 0
    else:
        return 0  # Tie


def minimax(board, depth, maximizing_player):
    """
    Minimax algorithm implementation.
    Returns the score and the sequence of moves leading to that score.
    """
    score = evaluate(board)
    if score != 0:
        return score, []

    if depth == 0:
        return 0, []

    if maximizing_player:
        max_eval = -math.inf
        best_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    eval, moves = minimax(board, depth - 1, False)
                    board[i][j] = EMPTY
                    if eval > max_eval:
                        max_eval = eval
                        best_moves = [(i, j)] + moves
        return max_eval, best_moves
    else:
        min_eval = math.inf
        best_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    eval, moves = minimax(board, depth - 1, True)
                    board[i][j] = EMPTY
                    if eval < min_eval:
                        min_eval = eval
                        best_moves = [(i, j)] + moves
        return min_eval, best_moves


def best_move(board):
    """
    Find the best move using the Minimax algorithm.
    """
    _, moves = minimax(board, 9, False)  # Depth limit set to maximum possible moves
    return moves


# Example usage
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

print("Initial board:")
for row in board:
    print(row)

moves = best_move(board)
print("Sequence of best moves for X:", moves)
