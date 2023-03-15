#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO269412
#
# Created:     16/10/2018
# Copyright:   (c) UO269412 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

 # 1. saber la opcion del usuario
 # 2. el ordenador debe elegir aleatoriamente piedra papel o tijera
 # 3. cuando sabemos las dos opciones tenemos que decidir quien gana

 # User         #Computer
 # piedra       piedra      E
 # piedra       papel       C
 # piedra       tijeras     U
 # papel        piedra      U
 # papel        papel       E
 # papel        tijeras     C
 # tijeras      piedra      C
 # tijeras      papel       U
 # tijeras      tijeras     E

import random

 # opc del usuario
user_opt = raw_input("Rock, scissors, paper?: ")

 # opc ordenador
computer_opt = random.randint(1,3)
 # 1 - rock
 # 2 - scissors
 # 3 - paper

if computer_opt == 1:
    computer_opt = "rock"
elif computer_opt == 2:
    computer_opt = "scissors"
else:
    computer_opt = "paper"

print("Computer chooses: {}".format(computer_opt))

if user_opt.lower() == "rock":
    if computer_opt == "rock":
        print("Draw")
    elif computer_opt == "scissors":
        print("User wins")
    else:
        print("Computer wins")

elif user_opt.lower() == "scissors":
    if computer_opt == "scissors":
        print("Draw")
    elif computer_opt == "paper":
        print("User wins")
    else:
        print("Computer wins")

elif user_opt.lower() == "paper":
    if computer_opt == "paper":
        print("Draw")
    elif computer_opt == "rock":
        print("User wins")
    else:
        print("Computer wins")

else:
    print("error")
