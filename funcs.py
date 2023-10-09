import turtle


def drawSquare(turt, color, length):
    turt.pencolor(color)
    for side in range(4):
        turt.forward(length)
        turt.left(90)


bob = turtle.Turtle()
drawSquare(bob, "blue", 20)
drawSquare(bob, "green", 120)
drawSquare(bob, "pink", 75)

sue = turtle.Turtle()
drawSquare(sue, "red", 50)
