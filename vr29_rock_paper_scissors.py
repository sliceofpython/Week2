"""
Rock Paper Scissors
By: VR29
"""

import random


computer = random.randint(1,3)

# print (computer)

"""
Choices
"""
while True:
    print("Rock, Paper or Scissors? ")
    choice = input()
    if choice.lower().startswith("r"):
        player = 1
        break

    elif choice.lower().startswith("p"):
        player = 2
        break

    elif choice.lower().startswith("s"):
        player = 3
        break

    else:
        print("That's not a valid option.")
        continue


if player == computer:
    print ("Draw")


elif player == 1:
    if computer == 2:
        print("You lose, paper covers rock.")

    else:
        print("You win, rock crushes scissors.")


elif player == 2:
    if computer == 1:
        print("You win, paper covers rock.")

    else:
        print("You lose, scissors cut paper.")

elif player == 3:
    if computer == 1:
        print("You lose, rock crushes scrissors.")

    else:
        print("You win, scrissors cut paper.")