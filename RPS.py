import random as r
import time as t

option = ["Rock", "Paper", "Scissors"]
win = [3,1,2]
lose = [2,3,1]

def isInt(value, boolean):
    """ 
        Used to determine if the input the user provides is valid.
        In this program, the user should only be entering whole numbers, or integers.
    """
    try:
        if int(value) <= 0 or int(value) >= 0:
            return True
    except ValueError:
        if boolean == True: #Only prints when player input is entered
            print("\"" + value + "\" is not a valid integer. Please try again.")
        return False

def main():
    """
        Used for easy looping of the program.
    """
    global option #allow the program to view the list made earlier in the program (was defined outside of the function I am now declaring)
    c = r.randint(1,3) #computer chooses what move it will make. Could also change this to a weighted system to have more likely outcomes.
    playerC = "" #Start with string to get loop initiated.
    while isInt(playerC, False) == False: #Loops while the player enters wrong input. Prints the provided input, and asks for the user to enter in new, valid input.
        print("[1] = Rock, [2] = Paper, [3] = Scissors")
        playerC = input("Please enter one of the option above: ")
        if isInt(playerC, True) == True:
            if int(playerC) > 3 or int(playerC) < 1: #Makes sure that the user enters in either rock, paper, or scissors.
                playerC = "" #Causes loop to restart
    playerC = int(playerC)
    if c == win[playerC-1]:
        print("You won. You picked [" + option[playerC-1] + "] and the computer picked [" + option[c-1] + "]")
    elif c == lose[playerC-1]:
        print("You lost. You picked [" + option[playerC-1] + "] and the computer picked [" + option[c-1] + "]") 
    else:
        print("You tied with the computer. You both picked [" + option[playerC-1] + "]")
    print("[1] = Yes, [Anything else] = No")
    restart = input(" -> ")
    if restart == "1":
        main()
    else:
        print("Ok. Quitting...")
        t.sleep(2)
        quit()
main() #Start for the first time.
