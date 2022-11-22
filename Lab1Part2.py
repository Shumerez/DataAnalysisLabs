import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import autograd

# create an empty figure with no Axes
mainFigure = plt.figure()
mainFigure.subplotpars.update(left = 0.05, bottom = 0.05) # manually add some space to see left & bottom axis

# add Axes named 'mainAxes' to the mainFigure
mainAxes = mainFigure.add_subplot()

# set limits for axis
mainAxes.set_ylim(-20, 20)
mainAxes.set_xlim(-20, 20)

# Equations 
# (1) f(x) = sin(x) * x
# (2) g(x) = f'(x)


# data
# x1 = np.linspace(-20, 20, 20) # Array of numbers in [-20..+20] for f(x)
x1 = torch.arange(-20, 20, 1).type(torch.float)

y1 = np.sin(x1) * x1  # equation №1

# x2 = np.linspace(-20, 20, 20) # Array of numbers in [-20..+20] for g(x)
x2 = torch.arange(-20, 20, 1).type(torch.float)

x2 = torch.tensor(x2, requires_grad = True).type(torch.float) # wrap array 'x' in tensor
x2 = x2.requires_grad_() # Say system what we want to store gradient

y2 = torch.sin(x2.dot(x2.T)) * x2.dot(x2.T)  # for equation №2
                                            # wtf is '.dot(x.T)' ???
print(y2)

# x3 = np.linspace(-20, 20, 1000)
x3 = torch.arange(-20, 20, 1).type(torch.float)
gradient = torch.tensor(x3) # wrap array 'x' in tensor

y2.backward(gradient)   # take derivative from f(x), I guess
                        # now we store f'(x) in x.grad. It is, kinda, 'gradient'?
                        # also tensor btw. So array of floats.
y2 = x2.grad
# print(x.grad)


# Create two plots of f(x) and g(x)
mainAxes.plot(x1, y1, label = 'f(x) = sin(x) * x') # troubleshooting
mainAxes.plot(x2.detach().numpy(), x2.grad, label = 'g(x) = f\'(x)')

# Add titles
mainAxes.set_title('Derivatives') # set Axes title

# Add labels
mainAxes.set_xlabel('x label')  # Add an x-label to the axes.
mainAxes.set_ylabel('y label')  # Add a y-label to the axes.

#Add legend
mainAxes.legend()

# Print graphics
plt.show()
