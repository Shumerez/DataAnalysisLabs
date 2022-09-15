import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import autograd

# create an empty figure with no Axes
mainFigure = plt.figure()
mainFigure.subplotpars.update(left = 0.05, bottom = 0.05) # manually add some space to see left & bottom axis

# add Axes named 'mainAxes' to the mainFigure
mainAxes = mainFigure.add_subplot() 

# Equations
# (1) f(x) = sin(x) * x
# (2) g(x) = f`(x)


# data
x = np.linspace(-20, 20) # Array of Xs

y1 = np.sin(x) * x # first equation

y2 = torch.tensor(y1.numpy()).backwards() # second equation




# Create two plots of F(x) and G(x)
mainAxes.plot(x, y1, label = 'func1')
mainAxes.plot(x, y2, label = 'func2')

# Add titles
mainAxes.set_title('SLE solution') # set Axes title

# Add labels
mainAxes.set_xlabel('x label')  # Add an x-label to the axes.
mainAxes.set_ylabel('y label')  # Add a y-label to the axes.

#Add legend
mainAxes.legend()

# Print graphics
plt.show()
