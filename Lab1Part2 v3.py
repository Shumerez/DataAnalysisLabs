import numpy as np
import matplotlib.pyplot as plt

import torch
from torch import autograd

x = torch.arange(4).type(torch.float)
print(x)

print(x.requires_grad)
x = x.requires_grad_()
print(x.requires_grad)
print(x.grad)

y = 2 * x.dot(x.T)
y2 = 2 * x.dot(x.T)

print(y)

print( y.backward() )


"""
# create an empty figure with no Axes
mainFigure = plt.figure()
mainFigure.subplotpars.update(left = 0.2, bottom = 0.2) # manually add some space to see left & bottom axis

# add Axes named 'mainAxes' to the mainFigure
mainAxes = mainFigure.add_subplot() 

# set limits for axis
mainAxes.set_ylim(-20, 20)
mainAxes.set_xlim(-20, 20)





# data
x = np.linspace(-20, 20, 5000) # Array of Xs

y1 = np.sin(x) * x # first equation

# Create two plots of F(x) and G(x)
mainAxes.plot(x, y1, label = 'f(x)')
#mainAxes.plot(x, y2, label = str(secondEquationInput[0]) + '* x + ' + str(secondEquationInput[1]) + '* y = ' + str(secondEquationInput[2]))


# Add titles
mainAxes.set_title('SLE solution') # set Axes title

# Add labels
mainAxes.set_xlabel('x label')  # Add an x-label to the axes.
mainAxes.set_ylabel('y label')  # Add a y-label to the axes.

#Add legend
mainAxes.legend()

# Print graphics
plt.show()

"""
