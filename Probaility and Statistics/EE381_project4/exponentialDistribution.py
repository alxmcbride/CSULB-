# PROBLEM 1b  The parameter value is beta =0.33

import numpy as np
import matplotlib.pyplot as plt

#PLOT THE Exponential PDF
def ExpPDF(beta):
  x=np.linspace(0, 4, 20)
  e=np.exp((-1/beta)*x)
  return(1/beta)*e

def exponential():

   #Generate the values of the RV X
   beta=0.33; n=10000;
   t=np.random.exponential(beta,n)
   print(t)

   #Create bins and histogram
   nbins=30; # Number of bins
   edgecolor='w'; # Color separating bars in the bargraph
   bins=[float(x) for x in np.linspace(0,4,20)]
   h1, bin_edges = np.histogram(t,bins,density=True)

  # Define points on the horizontal axis
   be1=bin_edges[0:np.size(bin_edges)-1]
   be2=bin_edges[1:np.size(bin_edges)]
   b1=(be1+be2)/2
   barwidth=b1[1]-b1[0] # Width of bars in the bargraph
   plt.close('all')


   # PLOT THE BAR GRAPH
   fig1=plt.figure(1)
   plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
   x1=np.linspace(0,4,20)
   y=ExpPDF(beta)
   plt.plot(x1,y,'r') #red line
   plt.title("PDF of a Exponentially Distributed Random Variable")
   plt.xlabel("Exponential Distribution of Random Variable T for n=10000")
   plt.ylabel("PDF")

   #Saving the file
   filename=input("Enter a name and extension (.pdf) to save the file as :")
   plt.savefig(filename)


   #CALCULATE THE MEAN AND STANDARD DEVIATION

   #Experimental
   mu_x=np.mean(t)
   print(mu_x)
   sig_x=np.std(t)
   print(sig_x)

exponential()