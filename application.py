# -*- coding: utf-8 -*

"""
In this code you can find a possible good solution of
python-guess-number, these project freedom
analyze and restructure, if you find a better way
applying an area in the code, you can comment it on Github Issues.
"""

import random # Module to generate random number

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

print instructions # Display instructions.

while countinue_all_game == True:
    random_number = random.randint(1, 20)
    print "++++++ %s ++++++" % random_number
    turn = 1 # Controls opportunities to guess number.
    countinue_turn = True # Controls if the turn continues.
    aceptChoise = False # Controls if the user want play again.

    # This "while" allows continue the turn.
    while countinue_turn == True:
        # This "try" controls the errors that occurred in the application.
        try:
            # Controls number of turn
            if turn <= 4:
                print "\n>>>> Your number turn is: %s <<<<" % turn
                user_input = raw_input("\n    * Please enter a number: ")

                # Verify if the input contains only numbers.
                if user_input.isdigit() == True:
                    user_input = int(user_input)

                    # Verify if input is one between twenty.
                    if user_input > 0 and user_input <= 20:

                            # Verify if input is equal to the guess number or more low or more hight.
                            if user_input == random_number:
                                print "\n\n    ((( ^.^ You Win!!! ^.^ )))"
                                print "\n\n Want to play again?"

                                # This "while" allows continue if the choice is incorrect.
                                while aceptChoise == False:
                                    try:
                                        choise = raw_input("\n\n please enter \"Y\" to play again or enter \"N\" to Exit: ")
                                        choise = choise.lower()

                                        if choise == "y":
                                            print "\n\n"
                                            print "+++++++++++++++++++++++"
                                            print "++++++ New Game! ++++++"
                                            print "+++++++++++++++++++++++"
                                            countinue_turn = False #Stops the turn.
                                            aceptChoise = True # When the choice is correct.
                                        elif choise == "n":
                                            print "\n   ((((   See you soon! XD  )))"
                                            countinue_turn = False # Stops the turn.
                                            countinue_all_game = False # Stops the game.
                                            aceptChoise = True # When the choice is correct.
                                        else:
                                            print "Your choice does not exist..."

                                    # Capture a bug in the play again
                                    except ValueError as error:
                                        print "Error ocurred: %s" % error

                            # Verify if user_input is more high
                            elif user_input > random_number:
                                print "    * You guessed too high, please try again"
                                turn += 1

                            # Verify if user_input is more low
                            elif user_input < random_number:
                                print "    * You guessed too low, please try again"
                                turn += 1
                    else:
                        print "    * You only can enter numbers the one to twenty"
                        turn += 1
                else:
                    print """\n
                    \r    * You can not enter letters, special caracters or decimal numbers; 
                    \r      Please enter a integer number"""
                    turn += 1
            else: # "else" if the user fail.
                print "\n\n    ###  Game Over!!! :C  ###"
                print "\t===>  The number to guess is %s  <===" % random_number
                print "\n\n Want to play again?"
                while aceptChoise == False:
                    try:
                        choise = raw_input("\n\n please enter \"Y\" to play again or enter \"N\" to Exit: ")
                        choise = choise.lower()

                        if choise == "y":
                            print "\n\n"
                            print "+++++++++++++++++++++++"
                            print "++++++ New Game! ++++++"
                            print "+++++++++++++++++++++++"
                            countinue_turn = False # Stops the turn.
                            aceptChoise = True # When the choice is correct.
                        elif choise == "n":
                            print "\n   ((((   See you soon! XD  )))"
                            countinue_turn = False # Stops the turn.
                            countinue_all_game = False # Stops the game
                            aceptChoise = True # When the choice is correct
                        else:
                            print "Your choice does not exist..."

                    # Capture a bug in the play again
                    except ValueError as error:
                        print "Error ocurred: %s" % error

        # Capture a bug in the game
        except ValueError as error:
            print " Error ocurred: %s, plese try again" % error