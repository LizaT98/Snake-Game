from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read()) # read returns a string, so we need to convert it into a number (int)
        self.color("white")
        self.penup()
        self.goto(0, 175)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def add_points(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        # reset the score to 0
        self.score = 0
        self.update_score()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)
