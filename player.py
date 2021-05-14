STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
