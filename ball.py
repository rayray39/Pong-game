from turtle import Turtle

TOP_EDGE_SCREEN = 285
BOTTOM_EDGE_SCREEN = -285

class Ball(Turtle) :

    def __init__(self, dx, dy) :
        super().__init__()
        self.dx = dx
        self.dy = dy
        self.original_dx = dx
        self.original_dy = dy
        self.shape("circle")
        self.penup()

    def move(self) :
        # detect collisions with top or bottom wall (depends on y_pos)
        if self.ycor() >= TOP_EDGE_SCREEN:
            self.dy *= -1
        elif self.ycor() <= BOTTOM_EDGE_SCREEN:
            self.dy *= -1

        x_pos = self.xcor() + self.dx
        y_pos = self.ycor() + self.dy

        self.setpos(x=x_pos, y=y_pos)

    def increment_speed(self) :
        self.dx *= 1.05
        self.dy *= 1.05

    def reset_state(self) :
        self.setpos(x=0, y=0)
        self.dx = self.original_dx
        self.dy = self.original_dy

    def getx(self) :
        # return current x coordinate of ball
        return self.xcor()
    
    def gety(self) :
        # return current y coordinate of ball
        return self.ycor()
        
    