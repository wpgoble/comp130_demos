import turtle

name = "Jack"
num = 24

bob = turtle.Turtle()
bob.pencolor("blue")
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)

print(f"Bob is at {bob.xcor()} {bob.ycor()}")

william = turtle.Turtle()
william.pencolor("red")
william.left(90)
william.forward(400)
x = round(william.xcor(), 1)
print(f"William is at {x} {round(william.ycor(), 2)}")
