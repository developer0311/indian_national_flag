import turtle


screen = turtle.Screen()
screen.screensize(800, 800)


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()