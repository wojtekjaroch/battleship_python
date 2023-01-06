
shots_board_content = "M"

match shots_board_content:
    case "M" or "S":
        print("Shot's coordinate already used !")
        # raise ValueError
    case "S":
        print("Shot's coordinate already used ! Ship already sunk is located here !")
        # raise ValueError

