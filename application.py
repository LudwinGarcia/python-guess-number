# -*- coding: utf-8 -*

"""
In this code you can find a possible good solution of
python-guess-number, these project freedom
analyze and restructure, if you find a better way
applying an area in the code, you can comment it on Github Issues.
"""

import random
import sys


instructions = """
################################################################
##                                                            ##
## The objective in this game is you can guess a number       ##
## in a range of one between twenty, first the game generates ##
## the number and after you can enter numbers to try guess,   ##
## when you enter the number, the game verify if your number  ##
## is more high or more lower than the generated number.      ##
##                                                            ##
## This is for help you to can create a strategy to guess     ##
## a number, you have four turns to complete the search.      ##
##                                                            ##
## You must be agile! Try it!!!                               ##
##                                                            ##
################################################################
"""

countinue_all_game = True # Controls if the application run again.

print instructions # Display instructions

while countinue_all_game == True:
    random_number = random.randint(1, 20)
    print "++++++ %s ++++++" % random_number
    turn = 1 # Controls opportunities to guess number
    countinue_turn = True
    aceptChoise = False

    while countinue_turn == True:
        # This "try" controls the errors that occurred in the application.
        try:
            if turn <= 4:
                print "\n>>>> Your number turn is: %s <<<<" % turn
                user_input = raw_input("\n    * Please enter a number: ")
                if user_input.isdigit() == True:
                    user_input = int(user_input)
                    # Verify if input is one between twenty 
                    if user_input > 0 and user_input <= 20:
                            if user_input == random_number:
                                print "    * You Win!!!"
                                print "\n\n Want to play again?"
                                while aceptChoise == False:
                                    try:
                                        choise = raw_input("\n\n please enter \"Y\" to play again or enter \"N\" to Exit: ")
                                        choise = choise.lower()
                                        if choise == "y":
                                            countinue_turn = False
                                            aceptChoise = True
                                        elif choise == "n":
                                            print "\n See you soon!"
                                            countinue_all_game = False
                                            countinue_turn = False
                                            aceptChoise = True
                                        else:
                                            print "Your choice does not exist..."
                                            pass
                                    except ValueError as error:
                                        print "Error ocurred: %s" % error
                            elif user_input > random_number:
                                print "    * You guessed too high, please try again"
                                turn += 1
                            elif user_input < random_number:
                                print "    * You guessed too low, please try again"
                                turn += 1
                    else:
                        print "    * You only can enter numbers the one to twenty"
                        turn += 1
                else:
                    print """
                    \r    * You can not enter letters, special caracters or decimal numbers; 
                    \r      Please enter a integer number"""
                    turn += 1
            else:
                countinue_turn = False
                countinue_all_game = False
        except ValueError as error:
            print " Error ocurred: %s, plese try again" % error