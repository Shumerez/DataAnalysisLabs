import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



mainAxes.set_title('SLE solution') # set Axes title
mainAxes.set_xlabel('label of X')  # set x-Axis label
mainAxes.set_ylabel('label of X')  # set y-Axis label

# If we want to tune ticks and tick labels, we should look Axis class documentation.
# If we want to change colors, linewidth and linestyle, we should look Artists class documentation.

x = np.linspace(-20, 20) # Define x axis (from ... to), how much discrete steps between
y = 2 * x                # the F(x) = y itself

mainAxes.plot(x, y)

plt.show()
