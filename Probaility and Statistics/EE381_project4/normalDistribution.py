#PROBLEM 1c The parameter values are mu=2.5 , sigma= 0.75

import numpy as np
import matplotlib.pyplot as plt

#PLOT THE Normal PDF
def gaussian(mu,sig):
 x = np.linspace(0, 5, 20)
 f=np.exp(-(x-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
 return f

def normal():
 # Generate the values of the RV X
 mu=2.5 ; sig=0.75; n=10000;
 x=np.random.normal(mu,sig,n)

# Create bins and histogram
 nbins=30; # Number of bins
 edgecolor='w'; # Color separating bars in the bargraph
 bins=[float(x) for x in np.linspace(0,5,20)]
 h1, bin_edges = np.histogram(x,bins,density=True)

# Define points on the horizontal axis
 be1=bin_edges[0:np.size(bin_edges)-1]
 be2=bin_edges[1:np.size(bin_edges)]
 b1=(be1+be2)/2
 barwidth=b1[1]-b1[0] # Width of bars in the bargraph
 plt.close('all')

# PLOT THE BAR GRAPH
 fig1=plt.figure(1)
 plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
 x1=np.linspace(0,5,20)
 # PLOT THE GAUSSIAN FUNCTION
 f=gaussian(mu,sig)
 plt.plot(x1,f,'r')
 plt.title("PDF of a Normal Random Variable")
 plt.xlabel("Normal Distribution of Random Variable X for n=10000")
 plt.ylabel("PDF")

 #Saving the file
 filename=input("Enter a name and extension (.pdf) to save the file as :")
 plt.savefig(filename)

 # CALCULATE THE MEAN AND STANDARD DEVIATION

 # Experimental
 mu_x = np.mean(x)
 print(mu_x)
 sig_x = np.std(x)
 print(sig_x)


normal()