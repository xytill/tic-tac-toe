def print_game(pass_matrix):
    print("---------")
    print("|", pass_matrix[11], pass_matrix[12], pass_matrix[13], "|")
    print("|", pass_matrix[21], pass_matrix[22], pass_matrix[23], "|")
    print("|", pass_matrix[31], pass_matrix[32], pass_matrix[33], "|")
    print("---------")
    return 0


def get_user_input(move):
    while 1:
        user_move = input("Enter the coordinates: ").replace(" ", "")
        if not user_move.isnumeric():
            print("You should enter numbers!")
        elif int(user_move) not in game_coordinates:
            print("Coordinates should be from 1 to 3!")
        elif game_matrix[int(user_move)] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            game_matrix[int(user_move)] = move
            print_game(game_matrix)
            game_values.clear()
            return check_game_state()
            break
    return 1


def check_game_state():
    game_values = list(game_matrix.values())

    xxx = ["X", "X", "X"]
    ooo = ["O", "O", "O"]

    grid_horizontal = [game_values[n:n+3] for n in range(0, len(game_values), 3)]
    grid_vertical = [game_values[n::3] for n in range(3)]
    grid_diagonal = [game_values[0], game_values[4], game_values[8]], [game_values[2], game_values[4], game_values[6]]

    check_x_wins = xxx in grid_horizontal or xxx in grid_vertical or xxx in grid_diagonal
    check_o_wins = ooo in grid_horizontal or ooo in grid_vertical or ooo in grid_diagonal

    count_x = game_values.count("X")
    count_o = game_values.count("O")
    count_blank = game_values.count(" ")

    if abs(count_x - count_o) > 1:
        print("Impossible")
    elif check_x_wins and check_o_wins:
        print("Impossible")
    elif check_x_wins:
        print("X wins")
        return 1
    elif check_o_wins:
        print("O wins")
        return 1
    elif count_blank == 0:
        print("Draw")
        return 1
    return 0


game_coordinates = (11, 12, 13, 21, 22, 23, 31, 32, 33)

game_values = list("         ")
game_matrix = dict(zip(game_coordinates, game_values))

print_game(game_matrix)
piece = "X"

while 1:
    if get_user_input(piece) != 0:
        break
    piece = "O" if piece == "X" else "X"
