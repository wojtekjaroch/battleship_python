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

ships_board =['X', 'o', 'O', 'Y', 'X']

ships_number_to_sink = ships_board.count('X')

print (ships_number_to_sink)

