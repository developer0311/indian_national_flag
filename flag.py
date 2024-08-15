from turtle import Turtle




flag_height = 200
flag_width = 300


class Flag(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fast")
        
        

    def block(self, color):
        self.pendown()
        self.begin_fill()
        self.color("black", color)
        for _ in range(2):
            self.forward(flag_height/3)
            self.right(90)
            self.forward(flag_width)
            self.right(90)
        self.forward(flag_height/3)
        self.end_fill()
        self.penup()



    def stand(self):
        self.goto(-300, -247.5)
        self.setheading(90)
        self.pendown()
        self.pencolor('brown')
        self.pensize(8)
        self.forward(550)
        self.penup()
        self.backward(flag_height + 10)
        self.setheading(0)
        self.forward(3)
        self.setheading(90)
        self.pensize(1)



    def stage(self):
        stage_height = 30
        self.color("black", "OrangeRed4")
        for i in range(3):
            self.goto(-350, -250 - (i * stage_height))
            self.setheading(0)
            self.begin_fill()
            for _ in range(2):
                self.pendown()
                self.forward(150 + (i * 20))
                self.right(90)
                self.forward(stage_height)
                self.right(90)
                self.penup()
            self.end_fill()



    def chakra_center(self):
        self.backward(flag_height/2)
        self.setheading(0)
        self.forward(flag_width/2)


    
    def draw_spokes(self):
        self.color("NavyBlue")
        self.pendown()
        self.pensize(2.5)
        for i in range(0, 360//2, 15):
            self.setheading(i)
            self.forward((flag_height/6) - 1)
            self.backward(((flag_height/6) - 1) * 2)
            self.forward((flag_height/6) - 1)
        self.color("white")
        self.dot(10)

        

    def draw_ashoka_chakra(self):
        self.chakra_center()
        self.pencolor("NavyBlue")
        self.dot(flag_height/3)
        self.pencolor("White")
        self.dot(flag_height/3 - 8)
        self.draw_spokes()