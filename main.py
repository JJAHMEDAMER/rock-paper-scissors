from random import choice

class rock_paper_scissor:
    def __init__(self) -> None:
        player = input("Chose ['p' paper - 'r' rock - 's' scissors]: " )
        robot = choice(['p', 's', 'r'])
        print("You " + player, " VS ", "Robot " + robot)
        if player == 'p' and robot == 'r' or player == 's' and robot == 'p' or player == 'r' and robot == 's':
            print("YOU WIN!!!")
        else:
            print("Better Luck")

play = rock_paper_scissor()