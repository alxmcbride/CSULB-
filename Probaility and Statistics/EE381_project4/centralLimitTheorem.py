# PROBLEM 2. The parameter values are:   a=2.0   cm;  b=5.0 cm
import numpy as np
import matplotlib.pyplot as plt

def gaussian(mu,sig,z):
  f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
  return f

def centralLimitTheorem():

 #Setting values f
 N=10000; nbooks=15; a=2.0; b=5.0;
 mu_w=(a+b)/2 ; sig_w=np.sqrt((b-a)**2/12)

 # Generate the values of the RV X
 X=np.zeros((N,1))
 for k in range(0,N):
  x=np.random.uniform(a,b,nbooks)
  w=np.sum(x)
  X[k]=w

# Create bins and histogram
 nbins=30; # Number of bins
 edgecolor='w'; # Color separating bars in the bargraph
 bins=[float(x) for x in np.linspace(nbooks*a, nbooks*b,nbins+1)]
 h1, bin_edges = np.histogram(X,bins,density=True)

# Define points on the horizontal axis
 be1=bin_edges[0:np.size(bin_edges)-1]
 be2=bin_edges[1:np.size(bin_edges)]
 b1=(be1+be2)/2
 barwidth=b1[1]-b1[0] # Width of bars in the bargraph
 plt.close('all')

# PLOT THE BAR GRAPH
 fig1=plt.figure(1)
 plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)

#PLOT THE PDF
 f=gaussian(mu_w*nbooks,sig_w*np.sqrt(nbooks),b1)
 plt.plot(b1,f,'r')
 plt.title("PDF of the Distribution of Random Variable for a stack with 15 books")
 plt.xlabel("Distribution of Random Variable Sn for n=15 books")
 plt.ylabel("PDF")

 #Saving the file
 filename=input("Enter a name and extension (.pdf) to save the file as :")
 plt.savefig(filename)
 mu_sn=mu_w*nbooks
 print(mu_sn)
 sig_sn=sig_w*np.sqrt(nbooks)
 print(sig_sn)

centralLimitTheorem()

