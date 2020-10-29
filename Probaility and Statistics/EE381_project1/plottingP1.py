import matplotlib.pyplot as plt
import numpy as np

def plotting(endpoint,outcomes,N,):
    # Setting the x values
    xRange = range(1, endpoint + 2)
    xSize = np.size(xRange)  # number of x values

    # Histogram to find final probabilities of each outcome
    hist, bin_edges = np.histogram(outcomes, bins=xRange)
    ticks = bin_edges[0:xSize - 1]
    plt.close('all')
    prob = hist / N

    # Plotting stem plot for PMF
    plt.stem(ticks, prob, use_line_collection=True)  # stem plot (x,y,...)

    # Labels for the plot
    plt.title('PMF for an n-sided die', fontsize=14,
          fontweight='bold')
    plt.xlabel('Number on the face of the die', fontsize=14)
    plt.ylabel('Probability', fontsize=14, )
    plt.xticks(ticks)
    filename=input("Enter a name and extension (.pdf) to save the file as :")
    plt.savefig(filename)