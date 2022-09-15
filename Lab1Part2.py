import numpy as np
import matplotlib.pyplot as plt

# create an empty figure with no Axes
mainFigure = plt.figure()
mainFigure.subplotpars.update(left = 0.05, bottom = 0.05) # manually add some space to see left & bottom axis

# add Axes named 'mainAxes' to the mainFigure
mainAxes = mainFigure.add_subplot() 

# Equations:
# (1) a11*x + a12*y = b1
# (2) a21*x + a22*y = b2
#
# a11 = setOfCoefficients1[0]; a12 = setOfCoefficients1[1]; b1 = setOfOrdinates[0]
# a21 = setOfCoefficients2[0]; a22 = setOfCoefficients2[1]; b2 = setOfOrdinates[1]

# inputs
setOfCoefficients1 = list(map(int,input("\nEnter first equation coefficients WITH SPACES like this 'a11 a12' : ").strip().split()))[:2]
setOfCoefficients2 = list(map(int,input("\nEnter second equation coefficients WITH SPACES like this 'a21 a22' : ").strip().split()))[:2]
setOfOrdinates = list(map(int,input("\nEnter equation's ordinates WITH SPACES like this 'b1 b2' : ").strip().split()))[:2]

# wrap arrays in np.array()
coefficientsSet = np.array( [setOfCoefficients1, setOfCoefficients2] )
setOfOrdinates = np.array(setOfOrdinates)

# calculate normal and expanded matrix ranks
rankOfMatrix = np.linalg.matrix_rank( [setOfCoefficients1, setOfCoefficients2] )
rankOfExpandedMatrix = np.linalg.matrix_rank( [ setOfCoefficients1 + [setOfOrdinates[0]], setOfCoefficients2 + [setOfOrdinates[1]] ] )
#print(rankOfMatrix, rankOfExpandedMatrix); # troubleshooting



# data
x = np.linspace(-20, 20) # Array of Xs
#print(setOfCoefficients1[0] / setOfCoefficients1[1], setOfOrdinates[0] / setOfCoefficients1[1]) # troubleshooting
#print(setOfCoefficients2[0] / setOfCoefficients2[1], setOfOrdinates[1] / setOfCoefficients2[1]) # troubleshooting

y1 = (setOfCoefficients1[0] * -x / setOfCoefficients1[1]) + (setOfOrdinates[0] / setOfCoefficients1[1]) # first equation
y2 = (setOfCoefficients2[0] * -x / setOfCoefficients2[1]) + (setOfOrdinates[1] / setOfCoefficients2[1]) # second equation

# troubleshooting
#print('check')
#print(setOfCoefficients1[0], setOfCoefficients1[1], ordinatesSet[0], setOfCoefficients1[0] * 1 / setOfCoefficients1[1], ordinatesSet[0] / setOfCoefficients1[1], )
#print( (setOfCoefficients1[0] * -1 / setOfCoefficients1[1]) + (ordinatesSet[0] / setOfCoefficients1[1]) )
#print(setOfCoefficients2[0] * 1 / setOfCoefficients2[1]) + (ordinatesSet[1] / setOfCoefficients2[1])

# Create two plots of F(x) and G(x)
mainAxes.plot(x, y1, label = str(setOfCoefficients1[0]) + '* x + ' + str(setOfCoefficients1[1]) + '* y = ' + str(setOfOrdinates[0]))
mainAxes.plot(x, y2, label = str(setOfCoefficients2[0]) + '* x + ' + str(setOfCoefficients2[1]) + '* y = ' + str(setOfOrdinates[1]))

# check for no and infinity solutions via Capelli theorem
if (rankOfMatrix != rankOfExpandedMatrix):                      # (1) No solutions
    print("No possible solutions")
    mainAxes.text(0, -5, "No possible solutions")
elif (rankOfMatrix != 2): # 2 - amount of unknown variables (x,y);(2) Infinity solutions
    print("Infinity possible solutions")
    mainAxes.text(0, -5, "Infinity possible solutions")
else:                                                           # (3) One solution
    # find answer matrix via np.linalg.solve()
    answerMatrix = np.linalg.solve(coefficientsSet, setOfOrdinates);

    # troubleshooting
    # print(setOfCoefficients1[0], '* x +', setOfCoefficients1[1], '* y = ', setOfOrdinates[0])
    # print(setOfCoefficients2[0], '* x +', setOfCoefficients2[1], '* y = ', setOfOrdinates[1])
    print(answerMatrix);

    # create dot plot to show solution
    mainAxes.scatter(answerMatrix[0], answerMatrix[1], label = 'solution')
    # add annotation
    mainAxes.annotate('solution (' + str(np.format_float_positional(answerMatrix[0], precision=2)) + '; ' + str(np.format_float_positional(answerMatrix[1], precision=2)) + ')',
                      xy=(answerMatrix[0], answerMatrix[1]), xytext=(answerMatrix[0], answerMatrix[1] - 5), arrowprops=dict(facecolor='black', shrink=0.05))

# Add titles
mainAxes.set_title('SLE solution') # set Axes title

# Add labels
mainAxes.set_xlabel('x label')  # Add an x-label to the axes.
mainAxes.set_ylabel('y label')  # Add a y-label to the axes.

#Add legend
mainAxes.legend()

# Print graphics
plt.show()
