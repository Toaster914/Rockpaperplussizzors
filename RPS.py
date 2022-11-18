'''
Toaster914
RPS 1.2
11/17/22
'''

import random, os

def rps_solver(mode):
    """
    Calculates for wins/losses. mode 1 for singleplayer. mode 2 for multiplayer.
    """
    global wins, losses, ties, p1_wins, p1_losses, p2_wins, p2_losses
    if mode == 1:
        if p1_choice == 1:
            if p2_choice == 1:
                    print("It's a tie! (R/R)")
                    ties += 1
            elif p2_choice == 2:
                    print("You lose. (R/P)")
                    losses += 1
            elif p2_choice == 3:
                    print("You win! (R/S)")
                    wins += 1
        elif p1_choice == 2:
            if p2_choice == 2:
                    print("It's a tie! (P/P)")
                    ties += 1
            elif p2_choice == 1:
                    print("You win! (P/R)")
                    wins += 1
            elif p2_choice == 3:
                    print("You lose. (P/S)")
                    losses += 1
        elif p1_choice == 3:
            if p2_choice == 3:
                    print("It's a tie! (S/S)")
                    ties += 1
            elif p2_choice == 1:
                    print("You lose. (S/R)")
                    losses += 1
            elif p2_choice == 2:
                    print("You win! (S/P)")
                    wins += 1
    elif mode == 2:
        if p1_choice == 1:
            if p2_choice == 1:
                    print("It's a tie! (R/R)")
                    ties += 1
            elif p2_choice == 2:
                    print("P2 Wins!. (R/P)")
                    p2_wins += 1
                    p1_losses += 1
            elif p2_choice == 3:
                    print("P1 Wins! (R/S)")
                    p1_wins += 1
                    p2_losses += 1
        elif p1_choice == 2:
            if p2_choice == 2:
                    print("It's a tie! (P/P)")
                    ties += 1
            elif p2_choice == 1:
                    print("P1 Wins! (P/R)")
                    p1_wins += 1
                    p2_losses += 1
            elif p2_choice == 3:
                    print("P2 Wins! (P/S)")
                    p2_wins += 1
                    p1_losses += 1
        elif p1_choice == 3:
            if p2_choice == 3:
                    print("It's a tie! (S/S)")
                    ties += 1
            elif p2_choice == 1:
                    print("P2 Wins!. (S/R)")
                    p2_wins += 1
                    p1_losses += 1
            elif p2_choice == 2:
                    print("P1 Wins! (S/P)")
                    p1_wins += 1
                    p2_losses += 1

loop = "Y"
master_loop = "Y"

while master_loop == "Y":
    wins = 0
    losses = 0
    ties = 0
    p1_wins = 0
    p1_losses = 0
    p2_wins = 0
    p2_losses = 0
    gamemode = 0
    loop = "Y"

    gamemode = int(input("Select a mode. 1 = against \"AI\" 2 = multiplayer >> "))

    if gamemode == 1:
        while loop == "Y" or loop == "y":

            p2_choice = random.randint(1, 3)

            #human input
            p1 = input("What is your choice (Rock, Paper Sizzors R,P,S (Case sensitive)) >> ")
            if p1 == "Rock" or p1 == "R":
                p1_choice = 1 #rock
            elif p1 == "Paper" or p1 == "P":
                p1_choice = 2 #paper
            elif p1 == "Sizzors" or p1 == "S":
                p1_choice = 3 #sizzors
            else:
                print("choose a real choice.")
            rps_solver(1)
            print("Wins: " + str(wins) + " Losses: " + str(losses) + " Ties: " + str(ties))
            gamemode_change = input("Change modes? (N to quit.) (Y/N) >> ")
            if gamemode_change == "y" or gamemode_change == "Y":
                loop = "n"
                break

    elif gamemode == 2:
        while loop == "Y" or loop == "y":
            p1 = input("Player 1, What is your choice (Rock, Paper Sizzors R,P,S (Case sensitive)) >> ")
            if p1 == "Rock" or p1 == "R":
                p1_choice = 1 #rock
            elif p1 == "Paper" or p1 == "P":
                p1_choice = 2 #paper
            elif p1 == "Sizzors" or p1 == "S":
                p1_choice = 3 #sizzors
            else:
                print("choose a real choice.")
            os.system("clear")
            p2 = input("Player 2, What is your choice (Rock, Paper Sizzors R,P,S (Case sensitive)) >> ")
            if p2 == "Rock" or p2 == "R":
                p2_choice = 1 #rock
            elif p2 == "Paper" or p2 == "P":
                p2_choice = 2 #paper
            elif p2 == "Sizzors" or p2 == "S":
                p2_choice = 3 #sizzors
            else:
                print("choose a real choice.")
            print()
            rps_solver(2)
            print()
            print("P1 Wins: " + str(p1_wins) + " P1 Losses: " + str(p1_losses))
            print("P2 Wins: " + str(p2_wins) + " P2 Losses: " + str(p2_losses))
            print("Ties: " + str(ties))
            print()
            gamemode_change = input("Change modes? (N to quit.) (Y/N) >> ")
            if gamemode_change == "y" or gamemode_change == "Y":
                loop = "n"
                break
            elif gamemode_change == "n" or gamemode_change == "N":
                print("Thanks for playing!")
                master_loop = "N"
                loop = "n"

