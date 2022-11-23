import torch
import matplotlib.pyplot as plt

# create an empty figure with no Axes
mainFigure = plt.figure()
mainFigure.subplotpars.update(left = 0.2, bottom = 0.2) # manually add some space to see left & bottom axis

# add Axes named 'mainAxes' to the mainFigure
mainAxes = mainFigure.add_subplot() 

# set limits for axis
#mainAxes.set_ylim(-20, 20)
#mainAxes.set_xlim(-20, 20)

# Create x array of numbers from -10 to 10 with 2000 steps-elements
x = torch.linspace(-10, 10, 2000, requires_grad = True)

# Our func
Y = x * torch.sin(x)

# some magic here
y = torch.sum(x * torch.sin(x))

# also magic
y.backward()

# Draw plots
mainAxes.plot(x.detach().numpy(), Y.detach().numpy(), label = 'f(x)=sin(x) * x')
mainAxes.plot(x.detach().numpy(), x.grad.detach().numpy(), label = 'g(x)=f\'(x)')

# Add grid
mainAxes.grid(True)

# Add labels
mainAxes.set_xlabel('x label')  # Add an x-label to the axes.
mainAxes.set_ylabel('y label')  # Add a y-label to the axes.

#Add legend
mainAxes.legend()

# Draw a plot actually
plt.show()

