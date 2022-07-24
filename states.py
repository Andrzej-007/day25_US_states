from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Courier", 18 , "normal")

class States(Turtle):

    def __init__(self, one_state, coordinates):
        super().__init__()

        self.penup()
        self.color('red')
        self.hideturtle()
        self.enter_state(one_state, coordinates)

    def enter_state(self, one_state, coordinates):
        self.goto(coordinates)
        self.write(f'{one_state}', align=ALIGMENT, font=FONT)

