import matplotlib.pyplot as plt
import numpy as np

def plotting(endpoint,outcomes,N,):
    # Setting the x values
    xRange = range(0, endpoint + 2)
    xSize = np.size(xRange)  # number of x values

    # Histogram to find final probabilities of each outcome
    hist, bin_edges = np.histogram(outcomes, bins=xRange)
    ticks = bin_edges[0:xSize - 1]
    plt.close('all')
    prob = hist / N

    # Plotting stem plot for PMF
    plt.stem(ticks, prob, use_line_collection=True)  # stem plot (x,y,...)

    # Labels for the plot
    plt.title('Bernoulli Trials: PMF - Experimental Results', fontsize=14,  #CHANGE THE TITLES FOR EACH PLOT AND FOR EACH CODE YOU PUT IN REPORT
          fontweight='bold')
    plt.xlabel('Number of successes in n=1000 trials', fontsize=14)
    plt.ylabel('Probability', fontsize=14, )
    plt.xticks(ticks)
    filename=input("Enter a name and extension (.pdf) to save the file as :")
    plt.savefig(filename)