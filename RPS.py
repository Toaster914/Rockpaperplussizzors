'''
Toaster914
RPS 1.1
10/4/22
'''

import random
loop = "Y"

while loop == "Y":

    p2_choice = random.randint(1, 3)

    #human input
    p1 = input("What is your choice (Rock, Paper Sizzors R,P,S (Case sensitive)): ")
    if p1 == "Rock" or p1 == "R":
        p1_choice = 1 #rock
    elif p1 == "Paper" or p1 == "P":
        p1_choice = 2 #paper
    elif p1 == "Sizzors" or p1 == "S":
        p1_choice = 3 #sizzors
    else:
        print("choose a real choice.")

    if p1_choice == 1:
        if p2_choice == 1:
            print("It's a tie! (R/R)")
        elif p2_choice == 2:
            print("You lose. (R/P)")
        elif p2_choice == 3:
            print("You win! (R/S)")
    elif p1_choice == 2:
        if p2_choice == 2:
            print("It's a tie! (P/P)")
        elif p2_choice == 1:
            print("You win! (P/R)")
        elif p2_choice == 3:
            print("You lose. (P/S)")
    elif p1_choice == 3:
        if p2_choice == 3:
            print("It's a tie! (S/S)")
        elif p2_choice == 1:
            print("You lose. (S/R)")
        elif p2_choice == 2:
            print("You win! (S/P)")
