import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import autograd

#x = np.linspace(-20, 20) # Array of floats in [-20..+20]


x = torch.tensor([3.0, 2.0, 1.5], requires_grad = True)
y = torch.pow(x, 2)

print(x.requires_grad)
print(y.requires_grad)

gradient = torch.tensor( [1.0, 1.0, 1.0] )
y.backward(gradient)

print(x.grad)