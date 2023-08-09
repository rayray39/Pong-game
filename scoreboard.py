from turtle import Turtle

Y_POSITION = 275
LENGTH_OF_ONE_DASH = 20
SCREEN_HEIGHT = 600

ALIGNMENT = "center"
FONT_FAMILY = "Arial"
FONT_SIZE = 15

class Scoreboard(Turtle) :

    def __init__(self, x_position, text, score_counter) :
        super().__init__()
        self.score_counter = score_counter
        self.text = text
        self.penup()
        self.hideturtle()
        self.goto(x=x_position, y=Y_POSITION)
        self.write(text + str(self.score_counter), align=ALIGNMENT, font=(FONT_FAMILY, FONT_SIZE, "normal"))

    def create_middle_line(self) :
        newTurtle = Turtle()
        newTurtle.penup()
        newTurtle.goto(x=0, y=-300)
        newTurtle.left(90)
        newTurtle.pendown()
        newTurtle.pensize(3)
        steps = SCREEN_HEIGHT // LENGTH_OF_ONE_DASH
        for i in range(steps) :
            newTurtle.penup()
            newTurtle.fd(LENGTH_OF_ONE_DASH)
            newTurtle.pendown()
            newTurtle.fd(LENGTH_OF_ONE_DASH)

    def increment_score(self) :
        self.score_counter += 1
        self.clear()
        self.write(self.text + str(self.score_counter), align="center", font=("Arial", 15, "normal"))


