def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t               Счет       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


def print_help():
    print("\tДля хода введите число от 1 до 9.")

    print("\t------------------")
    print("\t     Справка       ")
    print("\t------------------")

    print("\t     |     |")
    print("\t  1  |  2  |  3")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  4  |  5  |  6")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  7  |  8  |  9")
    print("\t     |     |")

    print("\tВам необходимо составить 3 крестика (нолика) в ряд, чтобы победить.\n"
          "\tСначала необходимо выбрать, кто будет ходить за Х, а кто за O.\n")


def check_win(player_pos, cur_player):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
            return True
    return False


def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


def single_game(cur_player):
    values = [' ' for x in range(9)]
    player_pos = {'X': [], 'O': []}
    while True:
        print_tic_tac_toe(values)
        try:
            print("Игрок ", cur_player, " выбирает: ", end="")
            move = int(input())
        except ValueError:
            print("Неверный ввод!!! Попробуйте снова.")
            continue

        if move < 1 or move > 9:
            print("Неверный ввод!!! Попробуйте снова.")
            continue

        if values[move - 1] != ' ':
            print("Место уже занято, выберите другое поле!")
            continue

        values[move - 1] = cur_player

        player_pos[cur_player].append(move)

        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Игрок ", cur_player, " побеждает!!!")
            print("\n")
            return cur_player

        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Ничья!")
            print("\n")
            return 'D'

        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == "__main__":
    print("Игрок 1")
    player1 = input("Введите имя: ")
    print("\n")

    print("Игрок 2")
    player2 = input("Введите имя: ")
    print("\n")

    cur_player = player1

    player_choice = {'X': "", 'O': ""}

    options = ['X', 'O']

    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    while True:
        print("Меню игрока", cur_player, ':')
        print("Введите 1, чтобы играть за X")
        print("Введите 2, чтобы играть за O")
        print("Введите 3, чтобы открыть справку")
        print("Введите 4, чтобы выйти")

        try:
            choice = int(input())
        except ValueError:
            print("Неверный ввод!!! Попробуйте снова.\n")
            continue

        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print_help()
            continue

        elif choice == 4:
            print("\t          Финальный счет")
            print_scoreboard(score_board)
            break

        else:
            print("Неверный ввод!!! Попробуйте снова.\n")

        winner = single_game(options[choice - 1])

        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1
