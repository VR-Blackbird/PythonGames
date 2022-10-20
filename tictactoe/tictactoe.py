from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|' + ' ' + ' ' + ' ' + str(board[0][0]) + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + str(
        board[0][1]) + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + str(board[0][2]) + ' ' + ' ' + ' ' + '|')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|' + ' ' + ' ' + ' ' + str(board[1][0]) + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + str(
        board[1][1]) + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + str(board[1][2]) + ' ' + ' ' + ' ' + '|')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|' + ' ' + ' ' + ' ' + str(board[2][0]) + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + str(
        board[2][1]) + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + str(board[2][2]) + ' ' + ' ' + ' ' + '|')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

    while True:
        user = int(input("User 2: "))
        for rows in range(len(board)):
            for col in range(len(board)):
                if board[rows][col] == user:
                    board[rows][col] = 'O'
                    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free = [(rows, col) for rows in range(len(board)) for col in range(len(board)) if board[rows][col] not in ['X', 'O']]
    return free


def victory_for(board):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    ss = [set(i) for i in board if len(set(i)) == 1]
    if len(ss) != 0:
        return list(ss[0])[0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return board[1][1]


def draw_move(board):
    # The function draws the computer's move and updates the board.

    while True:
        comp_inp = randrange(1, 10)
        for rows in range(len(board)):
            for col in range(len(board)):
                if board[rows][col] == comp_inp:
                    board[rows][col] = 'X'
                    return board


board = []
nums = list(range(1, 11))
m = 3
for i in range(1, 4):
    rows = list(range(nums[m] - 3, nums[m]))
    board.append(rows)
    m += 3

display_board(board)
while True:

    if victory_for(board) == 'O':
        print("O won the game")
        break

    board = draw_move(board)
    display_board(board)
    if victory_for(board) == 'X':
        print("X won the game")
        break
    elif not make_list_of_free_fields(board):
        print("Match Drawn")
        break
    board = enter_move(board)
    display_board(board)
