import numpy as np
import matplotlib.pyplot as plt

#Generate the values of the RV X
def singleBattery():
   beta=50; n=10000;
   t=np.random.exponential(beta,1)
   print(t)

   #Create bins and histogram
   nbins=30; # Number of bins
   edgecolor='w'; # Color separating bars in the bargraph
   bins=[float(x) for x in np.linspace(0,100,nbins)]
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
   # y=ExpPDF(beta)
   # plt.plot(x1,y,'r') #red line
   plt.title("PDF of a Exponentially Distributed Random Variable")
   plt.xlabel("Exponential Distribution of Random Variable T for n=10000")
   plt.ylabel("PDF")

   #Saving the file
   filename=input("Enter a name and extension (.pdf) to save the file as :")
   plt.savefig(filename)

singleBattery()