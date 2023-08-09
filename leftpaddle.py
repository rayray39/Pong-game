from paddle import Paddle

class Leftpaddle(Paddle) :

    def __init__(self, x_position, y_positions):
        super().__init__(x_position, y_positions)

    