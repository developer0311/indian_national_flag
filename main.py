from turtle import Screen
from flag import Flag
from background import Background




screen = Screen()
screen.screensize(800, 800)
screen.title("Indian National Flag")

background = Background()
background.ground("SpringGreen3")
background.sky("LightSkyBlue")
background.draw_bushes()


flag = Flag()
flag.stage()
flag.stand()
flag.block("green")
flag.block("white")
flag.block("orange")
flag.draw_ashoka_chakra()

screen.mainloop()
