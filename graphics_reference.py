import graphics

# get the radius from user
radius = input("How large do we want the circle to be? ")
radius = float(radius)

# create window to draw circle
window_size = radius * 10.2     # This is a random value I pick,
                                # since we are using radius, it will scale with
                                # the user input

# creating the window
half_window = window_size / 2
my_window = graphics.GraphWin("Example", window_size, window_size)
# setting coordinates to bottom left corner
my_window.setCoords(0, 0, window_size, window_size)
my_window.setBackground("white")    # gives us a white background

# Now we can create and draw the circle
center = graphics.Point(half_window, half_window)
my_circle = graphics.Circle(center, radius)
my_circle.setFill("#ee6a50")
my_circle.draw(my_window)

# After drawing the circle we'll wait for the user
# to click on the window before closing it and moving
# with the program
my_window.getMouse()
my_window.close()
