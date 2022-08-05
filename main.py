#! usr/bin/env python3

""" MAIN MODULE """

# from module import prodl, suml
# from sys import path
# from extra.iota import FunI
#
# l1 = [i for i in range(5)]
# l2 = [i for i in range(2,11, 2)]
#
# path.append("C:\\Users\\Admin\\Desktop\\Python\\python silver certification\\extra")
#
# for i in path:
#     print(i)
#
# print(FunI())


import pygame

run = True
width = 1000
height = 700
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("This is pygame By Jasffer", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False


##### SELF CREATED SPLIT FUNCTION #####

# def mysplit(strng):
#     splt_strng = []
#     splt_char = []
#
#     for ch in strng:
#         if ch.isspace():
#             if splt_char:
#                 splt_strng.append("".join(splt_char))
#                 splt_char = []
#         else:
#             splt_char.append(ch)
#
#     if splt_char:
#         splt_strng.append("".join(splt_char))
#         splt_char = []
#
#     return splt_strng
#
#
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))

##### SEVEN SEGMENT LED FUNCTION #####
# one = [" # ", " # ", " # ", " # ", " # "]
# two = ["###", "  #", "###", "#  ", "###"]
# three = ["###", "  #", "###", "  #", "###"]
# four = ["# #", "# #", "###", "  #", "  #"]
# five = ["###", "#  ", "###", "  #", "###"]
# six = ["###", "#  ", "###", "# #", "###"]
# seven = ["###", "  #", " # ", " # ", " # "]
# eight = ["###", "# #", "###", "# #", "###"]
# nine = ["###", "# #", "###", "  #", "  #"]
# zero = ["###", "# #", "# #", "# #", "###"]
#
#
# def seven_segment(data):
#     LED = {}
#     line1 = []
#     line2 = []
#     line3 = []
#     line4 = []
#     line5 = []
#     for n in data:
#         if n == "1":
#             LED[n] = one
#         elif n == "2":
#             LED[n] = two
#         elif n == "3":
#             LED[n] = three
#         elif n == "4":
#             LED[n] = four
#         elif n == "5":
#             LED[n] = five
#         elif n == "6":
#             LED[n] = six
#         elif n == "7":
#             LED[n] = seven
#         elif n == "8":
#             LED[n] = eight
#         elif n == "9":
#             LED[n] = nine
#         elif n == "0":
#             LED[n] = zero
#         else:
#             print("Invalid Syntax: Only numbers are accepted")
#             return
#             break
#
#     for i in LED:
#         line1.append(LED[i][0])
#         line2.append(LED[i][1])
#         line3.append(LED[i][2])
#         line4.append(LED[i][3])
#         line5.append(LED[i][4])
#
#     print(" ".join(line1))
#     print(" ".join(line2))
#     print(" ".join(line3))
#     print(" ".join(line4))
#     print(" ".join(line5))
#
#
# while True:
#     input_data = input("Please Enter a number: ")
#
#     if input_data == None or input_data == "":
#         break
#     else:
#         seven_segment(input_data)

##### BETTER VERSION OF THE SEVEN SEGMENT DISPLAY #####
# LED = {
#     "1": [" # ", " # ", " # ", " # ", " # "],
#     "2": ["###", "  #", "###", "#  ", "###"],
#     "3": ["###", "  #", "###", "  #", "###"],
#     "4": ["# #", "# #", "###", "  #", "  #"],
#     "5": ["###", "#  ", "###", "  #", "###"],
#     "6": ["###", "#  ", "###", "# #", "###"],
#     "7": ["###", "  #", " # ", " # ", " # "],
#     "8": ["###", "# #", "###", "# #", "###"],
#     "9": ["###", "# #", "###", "  #", "  #"],
#     "0": ["###", "# #", "# #", "# #", "###"]
# }
#
#
# def seven_segment(data):
#     lights = [LED[n] for n in data]
#
#     for i in range(5):
#         print(" ".join(light[i] for light in lights))
# while True:
#     input_data = input("Please Enter a number: ")
#
#     if input_data == None or input_data == "":
#         break
#     else:
#         seven_segment(input_data)

##### IMPROVED CAESAR CYPHER CODE
# while True:
#     txt = input("Input text: ")
#     skip = int(input("Input shift value: "))
#
#     if skip > 25 or skip < 1:
#         print("please only input a shift value not less than 1 nor greater than 25! \n")
#         continue
#     break
#
# cc = []
# for ch in txt:
#     dec = ord(ch)
#
#     # THE CHARACTER IS IN UPPERCASE
#     if dec < 91 and dec > 64:
#         alpha = dec + skip
#
#         if alpha <= 90:
#             cc.append(chr(alpha))
#
#         # IF THE CHARACTER IS GREATER THAN 90 RESTART FROM A
#         else:
#             alpha = (alpha - 90) + 64
#             cc.append(chr(alpha))
#     elif dec > 96 and dec < 123:
#         alpha = dec + skip
#
#         if alpha <= 122:
#             cc.append(chr(alpha))
#
#         # IF THE CHARACTER IS GREATER THAN 90 RESTART FROM A
#         else:
#             alpha = (alpha - 122) + 96
#             cc.append(chr(alpha))
#     else:
#         cc.append(ch)
#
# print("".join(cc))


##### PALINDROME WORD TESTER
# txt = input("Please enter a text: ")
# txt.upper()
# txt2 = ""
# counter = False
#
# txt.replace(" ", "")
#
# for i in range(len(txt2)):
#     if ord(txt2[i]) == ord(txt2[-i]):
#         continue
#
#     counter = True
#     break
#
# if not counter:
#     print("It's a palindrome")
# else:
#     print("It's not a palindrome")



##### ANAGRAM CHECKER
# first_word = input("Enter a text: ").upper()
# second_word = input("Enter the anagram of the text: ").upper()
#
# word1 = first_word.replace(" ", "")
# word2 = first_word.replace(" ", "")
#
# word1_checker = 0
# word2_checker = 0
#
# for i in range(len(word1)):
#     word1_checker += ord(word1[i])
#     word2_checker += ord(word2[i])
#
#     if word1_checker == word2_checker:
#         continue
#
#     print("Not anagrams")
#     break
#
# print("Anagrams")



##### DIGIT OF LIFE
# date = input("enter a date: ")
# stopper = 0
# counter = date
#
# while True:
#     for i in counter:
#         stopper += int(i)
#
#     if stopper > 9:
#         counter = str(stopper)
#         stopper = 0
#         continue
#
#     break
# 
# print(stopper)



##### FINDING THE POSITION OF A LETTER
# inpt1 = input("Please enter a text: ")
# inpt2 = input("Please enter another text: ")
#
# list1 = list(inpt1)
#
# for i in inpt2:
#     if i in list1:
#         list1.pop(inpt1.find(i))
#         inpt1 = "".join(list1)
#
# if not list1:
#     print("Yes")
# else:
#     print("No")



##### SODUKU GAME IN PYTHON
# soduku = {
#     0: "195743862",
#     1: "431865927",
#     2: "876192543",
#     3: "387459216",
#     4: "612387495",
#     5: "549216738",
#     6: "763524189",
#     7: "928671354",
#     8: "254938671",
# }
#
# squares = {
#     0: "".join(list(soduku[sq][0:3] for sq in range(3))),
#     1: "".join(list(soduku[sq][3:6] for sq in range(3))),
#     2: "".join(list(soduku[sq][6:] for sq in range(3))),
#     3: "".join(list(soduku[sq][0:3] for sq in range(3, 6))),
#     4: "".join(list(soduku[sq][3:6] for sq in range(3, 6))),
#     5: "".join(list(soduku[sq][6:] for sq in range(3, 6))),
#     6: "".join(list(soduku[sq][0:3] for sq in range(6, 9))),
#     7: "".join(list(soduku[sq][3:6] for sq in range(6, 9))),
#     8: "".join(list(soduku[sq][6:] for sq in range(6, 9))),
# }
#
# for i in range(9):
#     row = list(soduku[i])
#     column = list("".join(cols[i] for cols in soduku.values()))
#
#     for j in range(1, 10):
#         Error = False
#         # print(j,row,column,list(squares[i]), sep="\n", end="\n\n")
#         if str(j) not in row or str(j) not in column or str(j) not in list(squares[i]):
#             Error = True
#             break
#         else:
#             row.pop(row.index(str(j)))
#             column.pop(column.index(str(j)))
#
#     if Error:
#         print(f"Row and column {i} did not pass")
#         break
#
# if not Error:
#     print("Yes")



##### TRY EXCEPT EXERCISE
# def read_int(prompt, min, max):
#     try:
#         prompt = int(input())
#         assert prompt <= max
#         assert prompt >= min
#         return prompt
#     except ValueError:
#         print("Error: wrong input")
#     except:
#         print("Error: The value is not within permitted range (-10..10)")
#
#
# v = read_int("Enter a number from -10 to 10: ", -10, 10)
#
# print("The number is:", v)
