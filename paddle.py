from turtle import Turtle

TOP_EDGE_SCREEN = 285
BOTTOM_EDGE_SCREEN = -285

class Paddle(Turtle) :
    # a paddle is a Turtle
    # head turle is the one at the top
    # tail turtlr is the one at the bottom

    def __init__(self, x_position, y_positions) :
        super().__init__()
        self.x_position = x_position
        self.y_positions = y_positions
        self.hideturtle()  # hides the default turtle created in the center of the screen
        self.paddle = self.create_paddle(y_positions)

    def create_paddle(self, y_pos) :
        # x position for the turtles that create a single paddle is constant throughout
        res = []
        for i in range(len(y_pos)) :
            newTurtle = Turtle(shape="square")
            newTurtle.penup()
            newTurtle.goto(x=self.x_position, y=y_pos[i])
            res.append(newTurtle)
        return res

    def move_up(self) :
        # how the movement works: 
        # starts from the tail, the tail moves to the previous turtle's location
        # the next turtle then moves to the previous turtle's location, until the head turtle is reached
        # cannot move pass the top edge of screen
        for i in range(len(self.paddle)-1, -1, -1) :  # starts from tail and ends at head
            self.paddle[i].penup()
            curr_y_pos = self.paddle[i].ycor()
            new_y_pos = curr_y_pos + 20
            self.paddle[i].goto(self.x_position, new_y_pos)
        if self.paddle[0].ycor() >= TOP_EDGE_SCREEN:
            y_pos = TOP_EDGE_SCREEN
            for i in range(len(self.paddle)) :
                self.paddle[i].sety(y_pos)
                y_pos -= 20

    def move_down(self) :
        # how the movement works: 
        # starts from the head, the head moves to the next turtle's location
        # the next turtle then moves to the next turtle's location, until the tail turtle is reached
        # cannot move pass the bottom edge of screen
        for i in range(len(self.paddle)) :
            self.paddle[i].penup()
            curr_y_pos = self.paddle[i].ycor()
            new_y_pos = curr_y_pos - 20
            self.paddle[i].goto(self.x_position, new_y_pos)
        if self.paddle[-1].ycor() <= BOTTOM_EDGE_SCREEN:
            y_pos = BOTTOM_EDGE_SCREEN
            for i in range(len(self.paddle) - 1, -1, -1) :
                self.paddle[i].sety(y_pos)
                y_pos += 20

    def get_head_y(self) :
        # return head's current y coordinate
        return self.paddle[0].ycor()
    
    def get_tail_y(self) :
        # return tail's current y coordinate
        return self.paddle[-1].ycor()
