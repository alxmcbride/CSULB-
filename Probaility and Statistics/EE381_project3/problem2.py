import numpy as np
import math as m
import matplotlib.pyplot as plt

#PROBLEM 2: Bernoulli Trials using Binomial Formula

def problem2():
    n = 1000
    p=0.001
    q=1-p
    x=np.zeros((19,1))
    y=np.zeros((19,1))

    #Performing the calculation using the binomial formula
    for k in range(19):
        f=m.factorial(n)/(m.factorial(k)*m.factorial(n-k)) * (p**k) * (q**(1000-k))
        x[k]=k
        y[k]=f

    #Plotting the PMF
    plotting(x,y)

def plotting(x,y):
    # Setting the x values
    xRange = range(0,19)

    # Plotting stem plot for PMF
    plt.stem(x,y, use_line_collection=True)  # stem plot (x,y,...)

    # Labels for the plot
    plt.title('Bernoulli Trials: PMF - Binomial Formula', fontsize=14,  #CHANGE THE TITLES FOR EACH PLOT AND FOR EACH CODE YOU PUT IN REPORT
          fontweight='bold')
    plt.xlabel('Number of successes in n=1000 trials', fontsize=14)
    plt.ylabel('Probability', fontsize=14, )
    plt.xticks(xRange)
    filename=input("Enter a name and extension (.pdf) to save the file as :")
    plt.savefig(filename)

problem2()
