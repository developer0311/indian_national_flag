from turtle import Turtle




class Background(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        



    def ground(self, color):
        self.goto(x=-480, y=-400)
        self.color(color)
        self.setheading(90)
        self.begin_fill()
        for _ in range(2):
            self.forward(300)
            self.right(90)
            self.forward(960)
            self.right(90)
        self.end_fill()



    def sky(self, color):
        self.goto(x=-480, y=-100)
        self.color(color)
        self.setheading(90)
        self.begin_fill()
        for _ in range(2):
            self.forward(500)
            self.right(90)
            self.forward(960)
            self.right(90)
        self.end_fill()



    def draw_bush(self):
        self.setheading(90)
        self.pensize(3)
        self.forward(10)

        self.setheading(0)
        self.pendown()
        self.color("Green")
        self.begin_fill()
        self.circle(20)
        self.end_fill()

        self.setheading(90)
        # self.pensize(3)
        self.color("brown")
        self.backward(10)
        self.setheading(0)
        self.penup()
    


    def draw_bushes(self):
        self.setheading(0)
        self.forward(5)
        while self.xcor() <= 480:
            self.draw_bush()
            self.forward(50)  # Move to the right for the next bush
            


