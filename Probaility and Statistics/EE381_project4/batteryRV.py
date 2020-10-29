import matplotlib.pyplot as plt
import numpy as np

# PROBLEM 3. The parameter values are: beta =50 days; n=30 batteries; Y1=3 yrs; Y2=2 yrs; Y3=4 yrs;

def batteryRV():
    # Setting Values
    beta = 50; nBatteries = 30; N = 10000
    mu_c = nBatteries * beta;
    sig_c = np.sqrt(nBatteries) * beta

    #Generating C
    C=np.zeros((N,1))
    for i in range(0,N):
      t = np.random.exponential(beta,nBatteries);
      c=np.sum(t)
      C[i] = c

    # Create bins and histogram
    edgecolor = 'w';  # Color separating bars in the bargraph
    bins = [float(x) for x in np.linspace(0,3000,30)]
    h1, bin_edges = np.histogram(C, bins, density=True)

    # Define points on the horizontal axis
    be1 = bin_edges[0:np.size(bin_edges) - 1]
    be2 = bin_edges[1:np.size(bin_edges)]
    b1 = (be1 + be2) / 2
    barwidth = b1[1] - b1[0]  # Width of bars in the bargraph
    plt.close('all')


    # PLOT THE BAR GRAPH
    plt.bar(b1, h1,width=barwidth, edgecolor=edgecolor)

    # PLOT THE PDF
    #Experimental
    mu_e=np.mean(C)
    sig_e=np.std(C)
    x1=np.linspace(0, 3000, 30)
    f = gaussian(mu_e, sig_e, x1)
    plt.plot(x1, f, 'r')

    # Theoretical
    g = gaussian(mu_c, sig_c, x1)
    plt.plot(x1, g, 'g')
    plt.title("Distribution of Random Variable for the lifetime of a carton of 30 batteries")
    plt.xlabel("Distribution of Random Variable C in days")
    plt.ylabel("PDF")

    # Saving the file
    filename = input("Enter a name and extension (.pdf) to save the file as :")
    plt.savefig(filename)
    # mu_sn = mu_w * nbooks
    print(mu_c)
    # sig_sn = sig_w * np.sqrt(nbooks)
    print(sig_c)
    plt.close('all')

    #Plotting the CDF
    sum=np.cumsum(f)
    sum_0=np.append(0, sum)
    x1 = np.linspace(0,3000,len(sum_0))
    values=barwidth*sum_0
    plt.bar(x1,values,width=barwidth,edgecolor=edgecolor)
    plt.title("Distribution of Random Variable for the lifetime of a carton of 30 batteries")
    plt.xlabel("Distribution of Random Variable C in days")
    plt.ylabel("Probability")
    filename2 = input("Enter a name and extension (.pdf) to save the file as :")
    plt.savefig(filename2)


def gaussian(mu, sig, z):
    f = np.exp(-(z - mu) ** 2 / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    return f

batteryRV()
