import turtle

bob = turtle.Turtle()
bob.pencolor("blue")
bob.forward(100)
bob.left(90)
bob.forward(200)
x = round(bob.xcor(), 2)
y = round(bob.ycor(), 2)
print(f"Bob is at {x}, {y}")

sue = turtle.Turtle()
sue.pencolor("red")
sue.forward(50)
sue.right(90)
sue.forward(50)
x = round(sue.xcor(), 2)
y = round(sue.ycor(), 2)
print(f"Sue is at {x}, {y}")
