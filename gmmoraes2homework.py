import random
randomNumber = random.randrange(1, 3, 1)

numberList = ["rock","paper","scissors"]
computerChoice = numberList[randomNumber]
correct = False
while not correct:
    options = input("choose between rock, paper and scissors ")

    while options != "rock" and options!="paper" and options!="scissors":
        options = input("choose between rock, paper and scissors ")
    

   

    if options == "rock" and computerChoice == "scissors":
        print("You won" + "\n" + "your choice was " + options + " " +
                    "the computer chose " + computerChoice)
        correct = True
    elif options == "paper" and computerChoice == "rock":
        print("You won" + "\n" + "your choice was " + options + " " +
                    "the computer chose " + computerChoice)
        correct = True
    elif options == "scissors" and computerChoice == "paper":
        print("You won" + "\n" + "your choice was " + options + " " +
                    "the computer chose " + computerChoice)
        correct = True
    elif options == computerChoice:
        print("It is a draw" + "\n" + "your choice was " + options + " " +
                    "the computer chose " + computerChoice)
    else:
        print("You lost" + "\n" + "your choice was " + options + " " +
                    "the computer chose " + computerChoice)
        tryAgain = input("would you like to try again?")

        while tryAgain != "yes" and tryAgain !="no":
            tryAgain = input("would you like to try again?")
            
        if tryAgain == "yes":
            correct = False
        else:
            correct = True
        
