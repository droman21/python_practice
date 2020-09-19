from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie! Well, That's No Fun")
    elif player == "Rock":
        if computer == "Paper":
            print("Ouch! You Lose!", computer, "covers", player)
        else:
            print("Yippee You Win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Wahh Wahh You Lose!", computer, "cut", player)
        else:
            print("Woohoo! You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Oh! Sorry You Lose...", computer, "smashes", player)
        else:
            print("Schweeet You Win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False