from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        # self.highest_score = 0
        with open("new_file", mode='r') as file:
            content = int(file.read())
            self.highest_score = content

        self.score_update()


    def score_board(self):
        self.clear()
        self.write(f"your score: {self.score}, Record: {self.highest_score}", align="center")

    def score_update(self):
        self.score_board()
        self.score += 1


    # def game_over(self):
    #     self.clear()
    #     self.hideturtle()
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write("GAME OVER!", align="center", font=("Arial", 22, "normal"))

    def reset(self):
        if self.score >= self.highest_score:
            self.highest_score = self.score - 1
            with open("new_file", mode='w') as file:
                file.write(f"\n {self.highest_score}")
        else:
            pass
        self.score = 0
        self.score_update()
