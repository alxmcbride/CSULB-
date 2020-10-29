# PROBLEM 1a The parameter values are a=2.0  b=5.0
#

#


import numpy as np
import math
import matplotlib.pyplot as plt

#PLOT THE UNIFORM PDF
def UnifPDF(a,b,x):
 f=(1/abs(b-a))*np.ones(np.size(x))
 return f

def uniform():

   #Generate the values of the RV X
   a=2.0; b=5.0; n=10000;
   x=np.random.uniform(a,b,n)

   #Create bins and histogram
   nbins=30; # Number of bins
   edgecolor='w'; # Color separating bars in the bargraph
   bins=[float(x) for x in np.linspace(a, b,nbins+1)]
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
   f=UnifPDF(2.0,5.0,b1)
   plt.plot(b1,f,'r') #red line
   plt.title("PDF of a Uniform Random Variable")
   plt.xlabel("Uniform Distribution of Random Variable X for n=10000")
   plt.ylabel("PDF")

   #Saving the file
   filename = input("Enter a name and extension (.pdf) to save the file as :")
   plt.savefig(filename)

   #CALCULATE THE MEAN AND STANDARD DEVIATION

   #Theoretical
   Expct=(a+b) / 2
   print(Expct)
   SD = math.sqrt(((b-a)**2)/12)
   print(SD)

   #Experimental
   mu_x=np.mean(x)
   print(mu_x)
   sig_x=np.std(x)
   print(sig_x)

uniform()