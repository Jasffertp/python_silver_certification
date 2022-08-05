#seperate and end activity
"""
print("Hello", "my", "Name", 'Slim', "Shady", end=".. \n", sep="! ")
print("Hello my Name Slim Shady", end="..", sep="! ")

print("Programming","Essentials","in", sep="***", end="... \n")
print("Python")

print('    * \n   * * ')
print("  *   * ")
print(" *     * ")
print("***   *** ")
print("  *   * ")
print("  *   * ")
print("  ***** ")

short cut for comment in pyhthon: ctrl + /

"""



#Octal and hexamdecimal
"""
print(0o461)
print(0x123)
print(32e7)
"""


#Binary Activity
# print(True > False)
# print(True < False)


# Duration activity
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# 
# # Write your code here.
# hour = (((mins+dura)//60)+hour)%24
# mins = (mins+dura)%60
# 
# print(hour, ":", mins)


# x = 15//3
# print(x)



# for tax activity in reviewer:
# 
# 
# income = float(input("Enter the annual income: "))
# 
# if income < 85528:
#     tax = (income*.18)-556.2
# else:
#     income -= 85528
#     tax = 14839.2+(income*.32)
# 
# if tax <= 0:
#     tax = 0.0
# 
# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")


# activity for checking if the year is a leap year or common year
# 
# year = int(input("Enter a year: "))
# 
# if year < 1700:
#     print("Not within the Gregorian calendar period")
# elif year % 4 != 0:
#     print("Common year")
# elif year % 100 != 0:
#     print("Leap year")
# elif year %400 != 0:
#     print("Common year")
# else:
#     print("Leap year")


# acitivity for while loop to guess the secret number of the magician
# 
# secret_number = 777
# 
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# 
# num = int(input())
# 
# while num != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     num = int(input("What's the secret number? "))
# 
# print("Well done, muggle! You are free now.")


# activity for for loop counting the number of 5 seconds
# 
# import time
# 
# for i in range(1, 6):
#    print(i," Mississippi.")
#    time.sleep(1)
# 
# print("Ready or not here I come!")



# loop activity about being stuck on a while loop
# 
# while True:
#     word = input("please enter a word: ")
#     
#     if word == "chupacabra":
#         break
# 
# print("You've successfully left the loop.")



# activity about looping until a vowel is found for for loops
# 
# user_word = input("Please enter a word: ")
# user_word = user_word.upper()
# 
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     print(letter)


# upgraded vowel eating program for eating vowels and assigning the letters to one word
# 
# word_without_vowels = ""
# 
# user_word = input("please enter a word: ")
# user_word = user_word.upper()
# 
# 
# for letter in user_word:
#     if letter == "A":
#         continue
#     elif letter == "E":
#         continue
#     elif letter == "I":
#         continue
#     elif letter == "O":
#         continue
#     elif letter == "U":
#         continue
#     
#     word_without_vowels += letter
# 
# print(word_without_vowels)


# Block activity height counter
# blocks = int(input("Enter the number of blocks: "))
# 
# # My code
# height = 0
# layer = 0
# layer_ph = layer
# blocks_ph = blocks
# 
# while True:
#     if blocks_ph <= 0:
#         height = layer - 1
#         break
#     elif layer_ph == 0 and blocks_ph > 0:
#         height = 0
#         layer += 1
#         layer_ph = layer
#         blocks_ph = blocks
#         continue
#     elif blocks_ph > 0 and layer_ph > 0:
#         blocks_ph -= layer_ph
#         layer_ph -= 1
#         height += 1
#         print("the remaining blocks is ", blocks_ph, " at layer ", layer, " the remaining stack is ", layer_ph, " at height ", height)

# blocks = int(input("Enter the number of blocks: "))
# n = 1
# height = 0
# 
# while True:
#     blocks -= n
#     if blocks == 0:
#         height += 1
#         break
#     elif blocks < 0:
#         break
#     else:
#         n += 1
#         height += 1
#     
# 
# print("The height of the pyramid:", height)


# Code from the internet
# i=1
# layer=1
# height=0

# while i<blocks+1:
#     height+=layer
#     if height>blocks:
#         print(layer-1)
#         break
#     i+=1
#     layer+=1

# print("The height of the pyramid:", height)


# Colatz Hypothesis Activity
# c0 = int(input("input a number: "))
# counter = 0
# 
# while True:
#     if c0 == 1:
#         print(f"steps: {counter}")
#         break
#     
#     elif c0%2:
#         c0 = 3 * c0 + 1
#         counter += 1
#         print(c0)
#     
#     else:
#         c0 = c0//2
#         counter += 1
#         print(c0)

# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

# for i in range(1, 11):
#     if i%2:
#         print(i)
#         
#         
# x = 1
# while x < 11:
#     if x%2:
#         print(x)
#     x += 1
#     
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# The basics of Lists activity
# 
# # step 1
# beatles = []
# print("Step 1:", beatles)
# 
# # step 2
# beatles.append("John Lennon")
# beatles.append("George Harrison")
# beatles.append("Paul McCartney")
# print("Step 2:", beatles)
# 
# # step 3
# for i in range(2):
#     new = input("Add Stu Sutcliffe and Pete Best indicidually: ")
#     beatles.append(new)
#     
# print("Step 3:", beatles)
# 
# # step 4
# del beatles[-1]
# del beatles[-1]
# print("Step 4:", beatles)
# 
# # step 5
# beatles.insert(0, "Ringo Starr")
# print("Step 5:", beatles)
# 
# 
# # testing list legth
# print("The Fab", len(beatles))



# Bubble sorting activity O(2)
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
# 
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#         print(my_list)
# 
# print(my_list)


# 
# Checking whether a number is in a list activity
# 
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# print(f"The list without unique elements: {my_list}")
# 
# temp_list = []
# 
# for i in my_list[0:]:
#     if i not in temp_list:
#         temp_list.append(i)
# 
# for in in my_list[0:]:
#     if i in temp_list:
#         pass
#     else:
#         temp_list.append(i)
# 
# 
# print(f"The list with unique elements only: {temp_list}")

# WTF???!!!(not anymore)
# 
# my_list = [1,2,3]
# print(len(my_list))
# print(my_list[0], my_list[1], my_list[2])
# for i in range(len(my_list)):
#     print(my_list[i], i)
#     my_list.insert(1, my_list[i])
# 
# print(my_list)



# Checking how many days in a month and if the date is a leap year
# def is_year_leap(year):
#     if year < 1700:
#         return False
#     elif year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year %400 != 0:
#         return False
#     else:
#         return True
# 
# def days_in_month(year, month):
#     yr = is_year_leap(year)
#     
#     if month == 2 and yr:
#         return 29
#     elif month == 2 and not yr:
#         return 28
#     elif month >= 8 and not(month % 2):
#         return 31
#     elif month >=8 and month % 2:
#         return 30
#     elif month < 8 and not(month % 2):
#         return 30
#     else:
#         return 31
# 
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")



# Checks if number is a prime number:
# def is_prime(num):
#     for i in range(2, num):
#         num2 = num%i
#         #print(num,num2)
#         
#         if num2 == 0:
#             return False
#         else:
#             continue
#     
#     return True
#     
# for i in range(1, 20):
# 	if is_prime(i + 1):
# 			print(i + 1, end=" ")
# print()


# converting liters per 100km to miles per gallon
# def liters_100km_to_miles_gallon(liters):
#     gal = liters/3.785411784
#     mi = 100/1.609344
#     
#     return (mi/gal)
# 
# def miles_gallon_to_liters_100km(miles):
#     km = miles * 1.609344
#     km /= 100
#     
#     return(3.785411784/km)
# 
# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))
# 
# 
# import random
# 
# def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.
# #     
#     print("+-------+-------+-------+")
#     print("|       |       |       |")
#     print("| ", board[0][0],"   |   ", board[0][1]," |   ", board[0][2]," |")
#     print("|       |       |       |")
#     print("+-------+-------+-------+")
#     print("|       |       |       |")
#     print("| ", board[1][0],"   |   ", board[1][1]," |   ", board[1][2]," |")
#     print("|       |       |       |")
#     print("+-------+-------+-------+")
#     print("|       |       |       |")
#     print("| ", board[2][0],"   |   ", board[2][1]," |   ", board[2][2]," |")
#     print("|       |       |       |")
#     print("+-------+-------+-------+")
# #     
#     enter_move(board)
# # 
# def enter_move(board):
#     while True:
#         move = int(input("enter your move:"))
#         counter = False
#         if move >= 10 or move <= 0:
#             print("the number is invalid, choose another number")
#             continue
#         else:
#             for i in range(0,3):
#                 for j in range(0,3):
#                     if board[i][j] == move:
#                         board[i][j] = "O"
#                         counter = True
#                 
#                 if counter:
#                     break
#                 else:
#                     print("the number is invalid, choose another number")
#         if counter: break
#     
#     make_list_of_free_fields(board)
# 
# # 
# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.
#     list= []
#     for i in range(0,3):
#         for j in range(0,3):
#             if board[i][j] != "X" or board[i][j] != "O":
#                 tup = j
#                 list.append(tup)
# #     
#     victory_for(board, list)
# #     
# #     
# def victory_for(board, sign):
#      # The function analyzes the board status in order to check if 
# #     # the player using 'O's or 'X's has won the game
# #     
# #     
#     if not sign:
#         print("It's a tie")
#     elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
#         print("You lost!")
#     elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
#         print("You won!")
#     elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
#         print("You lost!")
#     elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
#         print("You lost!")
#     elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
#         print("You won!")
#     elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
#         print("You lost!")
#     elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
#         print("You won!")
#     elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
#         print("You Lost!")
#     elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
#         print("You Lost!")
#     elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
#         print("You Lost!")
#     elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
#         print("You won!")
#     else:
#         draw_move(board)
#  
# def draw_move(board):
#     # The function draws the computer's move and updates the board.
# #     
#     while True:
#         cpu = random.randint(1,9)
#         counter = False
#         for i in range(0,3):
#             for j in range(0,3):
#                 if board[i][j] == cpu:
#                     board[i][j] = "X"
#                     counter = True
#                     
#             if counter:
#                 break
#         if counter: break
#     display_board(board)
# #     
# #     
# # 
# # 
# board_display = [[1,2,3],[4,"X",6],[7,8,9]]
# display_board(board_display)


# print(10//5)

# x = 1
# y = 0
# 
# print(y^y)
# print(x^y)
# print(x^x)

N = int(input())
list = []

for i in range(N):
    order = input()
    
    action = ""
    
    for i in (order):
        if(i == " "):
            break
        action += i
        
            