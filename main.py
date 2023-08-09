from turtle import Turtle, Screen
from paddle import Paddle
from leftpaddle import Leftpaddle
from rightpaddle import Rightpaddle
from scoreboard import Scoreboard
from ball import Ball
import time

LEFT_EDGE_SCREEN = -287
RIGHT_EDGE_SCREEN = 282

# configure screen setup
screen = Screen()
screen.setup(width=600, height=600)  # set the dimensions of screen
screen.title("Welcome to a game of Pong!")
screen.tracer(n=0)

# create paddles
# both left and right paddles are Paddles, made of of 4 turtles (squares)
LEFT_Y_POSITIONS = [0, -20, -40, -60]  # y positions of the segments of the left paddle
LEFT_X_POSITION = -287
RIGHT_Y_POSITIONS = [0, -20, -40, -60]  # y positions of the segments of the right paddle
RIGHT_X_POSITION = 282

left_paddle = Leftpaddle(LEFT_X_POSITION, LEFT_Y_POSITIONS) 
right_paddle = Rightpaddle(RIGHT_X_POSITION, RIGHT_Y_POSITIONS)

# listen for any keyboard commands
screen.listen()  
screen.onkey(fun=left_paddle.move_up, key="w")  # left paddle up movement
screen.onkey(fun=left_paddle.move_down, key="s")  # left paddle down movement
screen.onkey(fun=right_paddle.move_up, key="Up")  # right paddle up movement
screen.onkey(fun=right_paddle.move_down, key="Down")  # right paddle down movement

# render scoreboards for both players
player1_score = Scoreboard(-150, "P1 Score: ", 0)
player2_score = Scoreboard(150, "P2 Score: ", 0)
middle_line = Scoreboard(0, "", "")
middle_line.create_middle_line()

# create ball
ball = Ball(5,5)

# game loop
game_is_on= True
while game_is_on :
    screen.update()
    time.sleep(0.05)

    ball.move()  # allow the ball to continuously move and bounce off top and bottom walls

    # detect ball collision with paddles, increase ball speed each time it bounces off the paddles 
    if right_paddle.get_tail_y() - 5 < ball.gety() < right_paddle.get_head_y() + 5 and ball.getx() >= RIGHT_EDGE_SCREEN - 22:
        # ball collision with right paddle
        ball.dx *= -1
        ball.increment_speed()
    elif left_paddle.get_tail_y() - 5 < ball.gety() < left_paddle.get_head_y() + 5 and ball.getx() <= LEFT_EDGE_SCREEN + 22:
        # ball collision with left paddle
        ball.dx *= -1
        ball.increment_speed()

    # render new scores
    if ball.getx() > RIGHT_EDGE_SCREEN :
        # if ball goes beyond right wall, make it go back to original state
        # which means that player 2 failed to return serve and player 1 gains a point
        ball.reset_state()
        player1_score.increment_score()
    elif ball.getx() < LEFT_EDGE_SCREEN :
        # if ball goes beyond left wall, make it go back to original state
         # which means that player 1 failed to return serve and player 2 gains a point
        ball.reset_state()
        player2_score.increment_score()

screen.exitonclick()