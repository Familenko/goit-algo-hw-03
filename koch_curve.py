import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()
