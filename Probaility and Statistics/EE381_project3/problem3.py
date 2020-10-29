import numpy as np
import matplotlib.pyplot as plt
import math

#PROBLEM 3: Bernoulli Trials by Poisson distribution

def problem3():
    n = 1000
    p = 0.001
    x = np.zeros((19, 1))
    y = np.zeros((19, 1))

    #Performing calculations using Poisson formula
    for k in range(19):
        lambdaVal=n*p
        f = (lambdaVal**k / math.factorial(k)) * math.exp(-lambdaVal)
        x[k] = k
        y[k] = f

    plotting(x, y)

def plotting(x,y):
    # Setting the x values
    xRange = range(0,19)
    xSize = np.size(xRange)  # number of x values

    # Plotting stem plot for PMF
    plt.stem(x,y, use_line_collection=True)  # stem plot (x,y,...)

    # Labels for the plot
    plt.title('Bernoulli Trials: PMF - Poisson Approximation', fontsize=14,  #CHANGE THE TITLES FOR EACH PLOT AND FOR EACH CODE YOU PUT IN REPORT
          fontweight='bold')
    plt.xlabel('Number of successes in n=1000 trials', fontsize=14)
    plt.ylabel('Probability', fontsize=14, )
    plt.xticks(xRange)
    filename=input("Enter a name and extension (.pdf) to save the file as :")
    plt.savefig(filename)

problem3()