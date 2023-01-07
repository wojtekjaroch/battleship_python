import os

CORRECT_INPUT_OPTION = ['a1', 'a2', 'a3', 'a4', 'a5', 
                        'b1', 'b2', 'b3', 'b4', 'b5', 
                        'c1', 'c2', 'c3', 'c4', 'c5',
                        'd1', 'd2', 'd3', 'd4', 'd5',
                        'e1', 'e2', 'e3', 'e4', 'e5', 'quit']

def get_empty_board():
    board = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"]
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
            if item == 'O':
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
  


def get_input_from_user():
    user_input = input('Please enter a position (A-E and 1-5) or enter \q\ to quit: ')
    return user_input

def validate_user_input(user_input):
    '''
    return True or False
    '''
    if user_input.lower() in CORRECT_INPUT_OPTION:
        return True
    else:
        print(f"This position - {user_input} is not valid. Please, choose a correct position!")
        return False

def quit_game(user_input):
    '''
    exit the program
    '''
    if user_input.lower() == 'q':
        exit()

def user_input_to_coordinates_with_validation(user_input):          
    user_input = user_input.lower()

    rows = {"a": 0, "b": 1, "c": 2, "d":3, "e":4}
    cols = {"1": 0, "2": 1, "3": 2, "4":3, "5":4}

    if len(user_input) == 2 and (user_input[0] in rows.keys() and user_input[1] in cols.keys()):
        row = rows[user_input[0]]
        col = cols[user_input[1]]
    else:
        row = 'ERR'
        col = 'ERR'
        print(f"This position - {user_input} is not valid. Please, choose a correct position!")

    return row, col



def mark_on_board(shots_board, ships_board, row, col):     #ma być zmienna przyjeta od gracza, chyba user_move ==> sprawdzić w testach
    
    range_of_search = [
                    ships_board[row+1][col],
                    ships_board[row-1][col],
                    ships_board[row][col+1],
                    ships_board[row][col-1]
                    ] # ToDo: testowanie przypadku kiedy strzelamy w skrajne pola

 
    try:
        if ships_board[row][col] == "X":
            match shots_board[row][col]:
                case "M":
                    print("Shot's coordinate already used !")
                    raise ValueError
                case "S":
                    print("Shot's coordinate already used ! Ship already sunk is located here !")
                    raise ValueError
                case "H":
                    print("Shot's coordinate already used ! Ship's part already hit is located here !")
                    raise ValueError                
                case "0":
                    if ships_board[row][col] == "X" and ships_board[row+1][col] != "X" and ships_board[row-1][col] != "X" and ships_board[row][col+1] != "X" and ships_board[row][col-1] != "X":
                        shots_board[row][col] == "S"
                        print("This is a hit! You sunk an opponent's ship")
                    elif ships_board[row][col] == "X" or ships_board[row+1][col] == "X" or ships_board[row-1][col] == "X" or ships_board[row][col+1] == "X" or ships_board[row][col-1] == "X":
                        shots_board[row][col] == "H"
                        print("This is a hit! But your opponent's ship is still sailing!")
                    return shots_board
                    



                    pass
                # case "H":
                #     pass
        
        
        
        
        
        
        
        
        
        elif ships_board[row][col] == "O":
                match shots_board[row][col]:
                    case "M":
                        print("Shot's coordinate already used !")
                        raise ValueError
                    case _:
                        print("Yu've missed !")
                        shots_board[row][col] = "M"

    except:
        pass

    elif shots_board[row][col] == "X" and shots_board[row+1][col] != "X" and shots_board[row-1][col] != "X" and shots_board[row][col+1] != "X" and shots_board[row][col-1] != "X":
        shots_board[row][col] == "S"
        print("This is a hit! You sunk an opponent's ship")
        return shots_board

    elif shots_board[row][col] == "X" or shots_board[row+1][col] == "X" or shots_board[row-1][col] == "X" or shots_board[row][col+1] == "X" or shots_board[row][col-1] == "X":
        shots_board[row][col] == "H"
        print("This is a hit! But your opponent's ship is still sailing!")
        return shots_board

    elif shots_board[row][col] == "X" or shots_board[row+1][col] == "H" or shots_board[row-1][col] == "H" or shots_board[row][col+1] == "H" or shots_board[row][col-1] == "H":
        shots_board[row][col] == "S"
        print("This is a hit! You sunk an opponent's ship")
        for i in range_of_search:
            if i == "H":
                i = "S" 
        return shots_board



# def get_human_coordinates(board):
#     while True:
#         user_input = get_input_from_user()
#         if validate_user_input(user_input):
#             if user_input.lower() == 'q':
#                 quit()
#             dict_user_input = user_input_to_coordinates(user_input)
#             #print(tuple_user_input, list_all_available_coordinates(board))
#             if check_available_coordinate(board, tuple_user_input):
#                 return tuple_user_input
#             else:
#                 warning_msg_already_taken()
#         else:
#             warning_message_outside_board()

# def warning_message_outside_board():
#     print('You choose wrong place on the board')

# def warning_msg_already_taken():
#     print('This position was already taken')        


def main():

    os.system('cls')

    # board = get_empty_board()


    players_1_ships_board = [
        ["X", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "X", "O", "O"],
        ["O", "O", "O", "X", "O"],
        ["O", "O", "O", "O", "O"]
        ]

    players_1_shots_board = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"]
        ]

    players_2_ships_board = [
        ["X", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "X", "O", "O"],
        ["O", "O", "O", "X", "O"],
        ["O", "O", "O", "O", "O"]
        ]

    players_2_shots_board = [
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O"]
        ]


    game_run_indicator = True
    player = 'Player 1'

    while game_run_indicator == True:

        match player:
            case "Player 1":
                shots_board = players_2_shots_board
                ships_board = players_2_ships_board
            case "Player 2":
                shots_board = players_1_shots_board
                ships_board = players_1_ships_board

        validation_indicator_2 = False
        while validation_indicator_2 == False:
            row , col = ['ERR' , 'ERR']
            while row == 'ERR' and col == 'ERR':
                validation_indicator_1 = False
                while validation_indicator_1 == False:
                    user_input = get_input_from_user()
                    validation_indicator_1 = validate_user_input(user_input)
                row, col = user_input_to_coordinates_with_validation(user_input)
            validation_indicator_2 = check_available_coordinate(shots_board, row, col)

        mark_on_board(shots_board, ships_board, row, col)

        match player:
            case "Player 1":
                players_2_shots_board = shots_board
            case "Player 2":
                players_1_shots_board = shots_board

        
        print (shots_board)



        match player:
            case 'Player 1':
                player = 'Player 2'
            case 'Player 2':
                player = 'Player 1'

        # game_run_indicator = True




if __name__ == '__main__':
    main()