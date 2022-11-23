import numpy as np
import matplotlib.pyplot as plt
import torch

# create an empty figure with no Axes
mainFigure = plt.figure()
mainFigure.subplotpars.update(left = 0.2, bottom = 0.2) # manually add some space to see left & bottom axis

# add Axes named 'mainAxes' to the mainFigure
mainAxes = mainFigure.add_subplot() 

# set limits for axis
mainAxes.set_ylim(-20, 20)
mainAxes.set_xlim(-20, 20)



#y.backward() 
#x.grad

# data
#x = np.linspace(-20, 20, 5000) # Array of Xs
x = torch.arange(-20, 20, 0.1)

x.clone().detach().requires_grad_(True)
#x = torch.tensor(x, requires_grad=True) #make a Tensor object out of x

y1 = np.sin(x) * x # first equation
y1.backward()

# Create two plots of F(x) and G(x)
mainAxes.plot(x, y1, label = 'f(x)')
#mainAxes.plot(x, y2, label = 'f'(x)')

# Add titles
mainAxes.set_title('SLE solution') # set Axes title

# Add labels
mainAxes.set_xlabel('x label')  # Add an x-label to the axes.
mainAxes.set_ylabel('y label')  # Add a y-label to the axes.

#Add legend
mainAxes.legend()

# Print graphics
plt.show()