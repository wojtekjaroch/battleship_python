import os

CORRECT_INPUT_OPTION = ['a1', 'a2', 'a3', 'a4', 'a5', 
                        'b1', 'b2', 'b3', 'b4', 'b5', 
                        'c1', 'c2', 'c3', 'c4', 'c5',
                        'd1', 'd2', 'd3', 'd4', 'd5',
                        'e1', 'e2', 'e3', 'e4', 'e5', 'quit']

def get_empty_board():
    board = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
        ]
    print(board)
    return board

def list_all_available_coordinates(board):

    '''
    lists all available coordinates from the board
    return list of tuples
    '''

    list_available_coordinates = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == '0':
                list_available_coordinates.append((row_index, item_index))
    return list_available_coordinates

def check_available_coordinate(board, row, col):
    '''
    check if user can put his sign in specific coordinates
    return True or False
    '''
    if (row, col) in list_all_available_coordinates(board):
        return True
    return False

# def get_input_from_human():
#     return input('Please choose place on board. ')
  


def get_input_from_user(player):
    user_input = input(f'{player} please enter a position (A-E and 1-5) or enter \q\ to quit: ')
    return user_input

def validate_user_input(user_input):
    '''
    return True or False
    '''
    if user_input.lower() in CORRECT_INPUT_OPTION:
        return True
    else:
        print(f'This position - {user_input} is not valid. Please, choose a correct position!')
        return False

def quit_game(user_input):
    '''
    exit the program
    '''
    if user_input.lower() == 'q':
        exit()

def user_input_to_coordinates_with_validation(user_input):          
    user_input = user_input.lower()

    rows = {'a': 0, 'b': 1, 'c': 2, 'd':3, 'e':4}
    cols = {'1': 0, '2': 1, '3': 2, '4':3, '5':4}

    if len(user_input) == 2 and (user_input[0] in rows.keys() and user_input[1] in cols.keys()):
        row = rows[user_input[0]]
        col = cols[user_input[1]]
    else:
        row = 'ERR'
        col = 'ERR'
        print(f'This position - {user_input} is not valid. Please, choose a correct position!')

    return row, col

def check_if_somebody_won(shots_board, ships_board):
    ships_number_to_sink = 0
    for ships_board_row in ships_board:
        ships_number_to_sink = ships_number_to_sink + ships_board_row.count('X')

    sunk_ships_number = 0
    for shots_board_row in shots_board:
        sunk_ships_number = sunk_ships_number + shots_board_row.count('S')

    if ships_number_to_sink == sunk_ships_number:
        return True
    else:
        return False




def mark_on_board(shots_board, ships_board, row, col):     #ma być zmienna przyjeta od gracza, chyba user_move ==> sprawdzić w testach
    
    range_of_search = [
                    ships_board[row+1][col],
                    ships_board[row-1][col],
                    ships_board[row][col+1],
                    ships_board[row][col-1]
                    ] # ToDo: testowanie przypadku kiedy strzelamy w skrajne pola
    if ships_board[row][col] == 'X':
        match shots_board[row][col]:
            case 'M':
                print('Shot\'s coordinate already used !')
                wheather_shots_repetion_necessary = True
            case 'S':
                print('Shot\'s coordinate already used ! Ship already sunk is located here !')
                wheather_shots_repetion_necessary = True
            case 'H':
                print('Shot\'s coordinate already used ! Ship\'s part already hit is located here !')
                wheather_shots_repetion_necessary = True                
            case '0':
                # ten if to przypadek jeżeli dookoła nie ma 'X'-ów
                if ships_board[row][col] == 'X' and ships_board[row+1][col] != 'X' and ships_board[row-1][col] != 'X' and ships_board[row][col+1] != 'X' and ships_board[row][col-1] != 'X':
                    shots_board[row][col] = 'S'
                    print('This is a hit! You sunk an opponent\'s ship')
                elif ships_board[row][col] == 'X' and (shots_board[row+1][col] == 'H' or shots_board[row-1][col] == 'H' or shots_board[row][col+1] == 'H' or shots_board[row][col-1] == 'H'):
                    shots_board[row][col] = 'S'
                    if shots_board[row+1][col] == 'H':
                        shots_board[row+1][col] = 'S'
                    elif shots_board[row-1][col] == 'H':
                        shots_board[row-1][col] = 'S'
                    elif shots_board[row][col+1] == 'H':
                        shots_board[row][col+1] = 'S'
                    elif shots_board[row][col-1] == 'H':
                        shots_board[row][col-1] = 'S'
                    print('This is a hit! You sunk an opponent\'s ship')
                elif ships_board[row][col] == 'X' and (ships_board[row+1][col] == 'X' or ships_board[row-1][col] == 'X' or ships_board[row][col+1] == 'X' or ships_board[row][col-1] == 'X'):
                    shots_board[row][col] = 'H'
                    print('This is a hit! But your opponent\'s ship is still sailing!')
                wheather_shots_repetion_necessary = False
    elif ships_board[row][col] == '0':
            match shots_board[row][col]:
                case 'M':
                    print('Shot\'s coordinate already used !')
                    wheather_shots_repetion_necessary = True
                case _:
                    print('You\'ve missed !')
                    shots_board[row][col] = 'M'
                    wheather_shots_repetion_necessary = False
    return shots_board, wheather_shots_repetion_necessary






def main():

    os.system('cls')

    # board = get_empty_board()


    players_1_ships_board = [
        ['X', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
        ]

    players_1_shots_board = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
        ]

    players_2_ships_board = [
        ['X', 'X', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', 'X', '0', '0'],
        ['0', '0', '0', 'X', '0'],
        ['0', '0', '0', '0', '0']
        ]

    players_2_shots_board = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
        ]



    player = 'Player 1'


    game_run_indicator = True   
    while game_run_indicator == True:
        match player:
            case 'Player 1':
                shots_board = players_1_shots_board
                ships_board = players_2_ships_board
            case 'Player 2':
                shots_board = players_2_shots_board
                ships_board = players_1_ships_board

        validation_indicator_2 = False
        while validation_indicator_2 == False:
            row , col = ['ERR' , 'ERR']
            while row == 'ERR' and col == 'ERR':
                validation_indicator_1 = False
                while validation_indicator_1 == False:
                    user_input = get_input_from_user(player)
                    if user_input == 'q':
                        quit_game()
                    validation_indicator_1 = validate_user_input(user_input)
                row, col = user_input_to_coordinates_with_validation(user_input)
            validation_indicator_2 = check_available_coordinate(shots_board, row, col)

        # try:

        wheather_shots_repetion_necessary = True
        while wheather_shots_repetion_necessary == True:
            shots_board, wheather_shots_repetion_necessary = mark_on_board(shots_board, ships_board, row, col)
            
            if check_if_somebody_won(shots_board, ships_board) == True:
                print(f'{player} won !')
                exit()

        # except:
        # print ('Error while marking on shot\'s board')

        match player:
            case 'Player 1':
                players_1_shots_board = shots_board
                player = 'Player 2'
            case 'Player 2':
                players_2_shots_board = shots_board
                player = 'Player 1'

        print (shots_board)



       

        # game_run_indicator = True




if __name__ == '__main__':
    main()