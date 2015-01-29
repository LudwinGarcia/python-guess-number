# -*- coding: utf-8 -*

"""
In this code you can find a possible good solution of
python-guess-number, these project freedom
analyze and restructure, if you find a better way
applying an area in the code, you can comment it on Github Issues.
"""

import random # Module to generate random number

INSTRUCTIONS = """
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

CONTINUE_ALL_GAME = True # Controls if the application run again.

print INSTRUCTIONS # Display INSTRUCTIONS.

while CONTINUE_ALL_GAME == True:
    RANDOM_NUMBER = random.randint(1, 20)
    print "++++++ %s ++++++" % RANDOM_NUMBER
    NUMBER_OF_TURN = 1 # Controls opportunities to guess number.
    CONTINUE_TURN = True # Controls if the turn continues.
    ACEPT_CHOICE = False # Controls if the user want play again.

    # This "while" allows continue the turn.
    while CONTINUE_TURN == True:
        # This "try" controls the errors that occurred in the application.
        try:
            # Controls number of turn
            if NUMBER_OF_TURN <= 4:
                print "\n>>>> Your number turn is: %s <<<<" % NUMBER_OF_TURN
                USER_INPUT = raw_input("\n    * Please enter a number: ")

                # Verify if the input contains only numbers.
                if USER_INPUT.isdigit() == True:
                    USER_INPUT = int(USER_INPUT)

                    # Verify if input is one between twenty.
                    if USER_INPUT > 0 and USER_INPUT <= 20:

                        # Verify if input is equal to the guess number or low or hight.
                        if USER_INPUT == RANDOM_NUMBER:
                            print "\n\n    ((( ^.^ You Win!!! ^.^ )))"
                            print "\n\n Want to play again?"

                            # This "while" allows continue if the choice is incorrect.
                            while ACEPT_CHOICE == False:
                                try:
                                    print '''
                                    \r Please enter "Y" to play again or enter "N" to Exit:'''
                                    CHOICE = raw_input(" > ")
                                    CHOICE = CHOICE.lower()

                                    if CHOICE == "y":
                                        print "\n\n"
                                        print "+++++++++++++++++++++++"
                                        print "++++++ New Game! ++++++"
                                        print "+++++++++++++++++++++++"
                                        CONTINUE_TURN = False #Stops the turn.
                                        ACEPT_CHOICE = True # When the choice is correct.
                                    elif CHOICE == "n":
                                        print "\n   ((((   See you soon! XD  )))"
                                        CONTINUE_TURN = False # Stops the turn.
                                        CONTINUE_ALL_GAME = False # Stops the game.
                                        ACEPT_CHOICE = True # When the choice is correct.
                                    else:
                                        print "Your choice does not exist..."

                                # Capture a bug in the play again
                                except ValueError as error:
                                    print "Error ocurred: %s" % error

                        # Verify if USER_INPUT is more high
                        elif USER_INPUT > RANDOM_NUMBER:
                            print "    * You guessed too high, please try again"
                            NUMBER_OF_TURN += 1

                        # Verify if USER_INPUT is more low
                        elif USER_INPUT < RANDOM_NUMBER:
                            print "    * You guessed too low, please try again"
                            NUMBER_OF_TURN += 1
                    else:
                        print "    * You only can enter numbers the one to twenty"
                        NUMBER_OF_TURN += 1
                else:
                    print """\n
                    \r    * You can not enter letters, special caracters or decimal numbers; 
                    \r      Please enter a integer number"""
                    NUMBER_OF_TURN += 1
            else: # "else" if the user fail.
                print "\n\n    ###  Game Over!!! :C  ###"
                print "\t===>  The number to guess is %s  <===" % RANDOM_NUMBER
                print "\n\n Want to play again?"
                while ACEPT_CHOICE == False:
                    try:
                        print '''
                        \r Please enter "Y" to play again or enter "N" to Exit:'''
                        CHOICE = raw_input(" > ")

                        if CHOICE == "y":
                            print "\n\n"
                            print "+++++++++++++++++++++++"
                            print "++++++ New Game! ++++++"
                            print "+++++++++++++++++++++++"
                            CONTINUE_TURN = False # Stops the turn.
                            ACEPT_CHOICE = True # When the choice is correct.
                        elif CHOICE == "n":
                            print "\n   ((((   See you soon! XD  )))"
                            CONTINUE_TURN = False # Stops the turn.
                            CONTINUE_ALL_GAME = False # Stops the game
                            ACEPT_CHOICE = True # When the choice is correct
                        else:
                            print "Your choice does not exist..."

                    # Capture a bug in the play again
                    except ValueError as error:
                        print "Error ocurred: %s" % error

        # Capture a bug in the game
        except ValueError as error:
            print " Error ocurred: %s, plese try again" % error
