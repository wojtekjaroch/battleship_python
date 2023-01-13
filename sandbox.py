import os
os.system('cls')

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

# shots_board_content = "M"

# match shots_board_content:
#     case "M" or "S":
#         print("Shot's coordinate already used !")
#         # raise ValueError
#     case "S":
#         print("Shot's coordinate already used ! Ship already sunk is located here !")
#         # raise ValueError

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

# Testowa_Zm_1 = 300
# Testowa_Zm_2 = 500
# Testowa_Zm_3 = 500

# if Testowa_Zm_1 == 300 and (Testowa_Zm_2 == 200 or Testowa_Zm_3 == 200):
#     print("OK")
# else:
#     print("nieOK")

#---------------------------------------------------------------------------------------------------

# Testowa_Zm_1 = 100
# Testowa_Zm_2 = 500
# Testowa_Zm_3 = 600

# if Testowa_Zm_1 == 100 or Testowa_Zm_2 == 200 or Testowa_Zm_3 == 200:
#     print("OK")
# else:
#     print("nieOK")

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

# imie_kuzyna = 'Józek'

# match imie_kuzyna:
#     case 'Józek':
#         pass
#     case 'Stefan':
#         pass
#     case 'Zbyszek':
#         pass

#---------------------------------------------------------------------------------------------------

# imie_kuzyna = 'Zbyszek'
# imie_babci = 'Henia'

# if imie_kuzyna == 'Konrad':
#         print ('imie_kuzyna OK')
# elif imie_babci == 'Henia':
#         print ('imie_babci OK')



# print('koniec')


#---------------------------------------------------------------------------------------------------

# na konsultacje

# imie_kuzyna = 'Zbyszek'
# imie_babci = 'Henia'

# match imie_kuzyna and imie_babci:
#     case 'ZbyszekHenia':
#         print ('OK')
#     case 'Stefan':
#         pass
#     case 'Zbyszek':
#         pass

# print('koniec')


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

# ships_board =['X', 'o', 'O', 'Y', 'X']

# ships_number_to_sink = ships_board.count('X')

# print (ships_number_to_sink)


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------



# def display_board(fields_of_board_content):

#   board = (f"""
#       1   2   3
#   A   {fields_of_board_content[0][0]} | {fields_of_board_content[0][1]} | {fields_of_board_content[0][2]} 
#   B   {fields_of_board_content[1][0]} | {fields_of_board_content[1][1]} | {fields_of_board_content[1][2]} 
#   C   {fields_of_board_content[2][0]} | {fields_of_board_content[2][1]} | {fields_of_board_content[2][2]} 
#   """)

#   print(f'\nCurrent bord layout:\n{board}')
# a = 1
# b = 2
# def multiply(a, b):
#   a = float(a)
#   b = float(b)
#   c = a *b
#   print(c)
# 
# a = float(input("Please, input the first number"))
# b = float(input("Please, input the second number"))
# c = a * b
# print(c)

def multiply(a, b):
  while True:
    a = float(input("Please, input the first number"))
    b = float(input("Please, input the second number"))
    c = a * b
    print(c)
    return c
multiply(a, b)


