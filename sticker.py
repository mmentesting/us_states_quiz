from turtle import Turtle

class Sticker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def state_sticker(self, position, state):
        self.setposition(position)
        self.write(state)
