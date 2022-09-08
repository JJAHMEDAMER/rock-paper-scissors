from random import choice

class rock_paper_scissor:
    def __init__(self) -> None:
        score = [0, 0]
        playing = 'y'
        while playing == 'y':
            player = input("Chose ['p' paper - 'r' rock - 's' scissors]: " )
            robot = choice(['p', 's', 'r'])
            print("You " + player, " VS ", "Robot " + robot)
            if player == 'p' and robot == 'r' or player == 's' and robot == 'p' or player == 'r' and robot == 's':
                print("YOU WIN!!!")
                score[0] += 1
            elif player == robot:
                print("Tie")
            else:
                print("Better Luck")
                score[1] += 1
            print("Score: ", score)
            playing = input("Play Again?(y/n): ")
                

play = rock_paper_scissor()