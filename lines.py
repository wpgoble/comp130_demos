import matplotlib.pyplot as plt
import numpy as np

# Don't worry about this
# Here we are just generating values to plot
X = np.linspace(0, 100, 10)
Y = np.zeros(10)

plt.plot(X, Y+0, "b:", linewidth=1.5)  # Blue dotted line
plt.plot(X, Y+1, "r-", linewidth=1.5)  # Red solid line
plt.plot(X, Y+2, "g--", linewidth=1.5) # Green dashed line
plt.plot(X, Y+3, "c-.", linewidth=1.5) # Cyan dashdot line
plt.show()

# Colors
#--------------------
# b         | blue
# g         | green
# r         | red
# c         | cyan
# m         | magenta
# y         | yellow
# k         | black
# w         | white
#---------------------
# We can also use
# color='#eeefff'
# to specify an exact RBG value
